/*
 * If not stated otherwise in this file or this component's Licenses.txt file the
 * following copyright and licenses apply:
 *
 * Copyright 2016 RDK Management
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 * http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
*/

#include "pam.h"
#include "ssp_tdk_wrp.h"

/* To provide external linkage to C Functions defined in TDKB Component folder */

extern "C"
{
int ssp_register(bool);
int ssp_terminate();
GETPARAMVALUES* ssp_getParameterValue(char* pParamName,int* pParamsize,int *pRet);
int ssp_setParameterValue(char *pParamName,char *pParamValue,char *pParamType, int commit);
int ssp_CRRestart();
GETPARAMNAMES *ssp_getParameterNames(char* pPathName,int recursive,int* pParamSize);
void free_Memory_Names(int size,GETPARAMNAMES *Freestruct);
void free_Memory_val(int size,GETPARAMVALUES *Freestruct);
void free_Memory_Attr(int size,GETPARAMATTR *Freestruct);
};

/***************************************************************************
 *Function name	: initialize
 *Description	: Initialize Function will be used for registering the wrapper method
 *        	  with the agent so that wrapper function will be used in the script
 *
 *****************************************************************************/

bool pam::initialize(IN const char* szVersion)
{
    DEBUG_PRINT(DEBUG_TRACE,"TDK::pam Initialize\n");
    return TEST_SUCCESS;
}

/***************************************************************************
 *Function name : testmodulepre_requisites
 *Description   : testmodulepre_requisites will  be used for setting the
 *                pre-requisites that are necessary for this component
 *
 *****************************************************************************/
std::string pam::testmodulepre_requisites()
{
    int returnValue;
    returnValue = ssp_register(1);

    if(0 != returnValue)
    {
        DEBUG_PRINT(DEBUG_TRACE,"\n testmodulepre_requisites: Failed to initialize \n");
        return "TEST_FAILURE";
    }

    return "SUCCESS";
}

/***************************************************************************
 *Function name : testmodulepost_requisites
 *Description   : testmodulepost_requisites will be used for resetting the
 *                pre-requisites that are set
 *
 *****************************************************************************/
bool pam::testmodulepost_requisites()
{
    DEBUG_PRINT(DEBUG_LOG,"testmodulepost_requisites() \n");
    return 0;
}


/***************************************************************************
 *Function name : pam_GetParameterNames
 *Descrption    : pam Component Get Param Name API functionality checking
 *
 * @param [in]  req - ParamName : Holds the name of the parameter
 * @param [in]  req - ParamList : Holds the List of the parameter
 * @param [out] response - filled with SUCCESS or FAILURE based on the return value
 *****************************************************************************/
void pam::pam_GetParameterNames(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"Inside Fucntion GetParamNames \n");
    string ParamName=req["ParamName"].asCString();
    string ParamList=req["ParamList"].asCString();
    int size=0,i=0;
    int size_ret=0;
    GETPARAMNAMES *DataValue;
    GETPARAMNAMES *DataValue1;
    DataValue=ssp_getParameterNames(&ParamName[0],1,&size_ret);
    if(NULL==DataValue)
    {
        response["result"] = "FAILURE";
        response["details"] = "Get Param Name for Parameter returned NULL";
        return;
    }
    DataValue1=ssp_getParameterNames(&ParamList[0],0,&size);
    if(NULL==DataValue1)
    {
        printf("Get Param Name for ParameterList returned NULL\n");
        free_Memory_Names(size_ret,DataValue);
    }
    else
    {
        for(i=0;i<size;i++)
        {
            if(strcmp(DataValue1[i].pParamNames,DataValue[0].pParamNames)==0)
            {
                if(DataValue[0].writable==DataValue1[i].writable)
                {
                    free_Memory_Names(size,DataValue1);
                    printf("Parameter Name has been fetched successfully and it matched with parameter List\n");
                    response["result"] = "SUCCESS";
		    response["details"] = DataValue[0].pParamNames;
                    return;
                }
                else
                {

                    free_Memory_Names(size,DataValue1);
                    printf("Parameter attributes does not match with the parameter List\n");
                    response["result"] = "FAILURE";
                    response["details"] = "Parameter Name and its attributes does not match with the parameter List";
                    return;
                }
            }
        }
        free_Memory_Names(size,DataValue1);
        response["result"] = "FAILURE";
        response["details"] = "Parameter Name does not match with the paramters in paramter list";
	return;
    }

}

/***************************************************************************
 *Function name : pam_GetParameterValues
 *Descrption    : pamPa Component Get Param Value API functionality checking
 *
 * @param [in]  req - ParamName : Holds the name of the parameter
 * @param [out] response - filled with SUCCESS or FAILURE based on the return value
 *****************************************************************************/
void pam::pam_GetParameterValues(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"Inside Function GetParamValues \n");
    int size_ret=0;
    GETPARAMVALUES *DataParamValue;
    int getRet = 0;

    string ParamName=req["ParamName"].asCString();
    DataParamValue=ssp_getParameterValue(&ParamName[0],&size_ret,&getRet);
    if((DataParamValue == NULL))
    {
        printf("GetParamValue funtion returns NULL as o/p\n");
    }
    else
    {
        DEBUG_PRINT(DEBUG_TRACE,"Parameter Values are as :\n");
            DEBUG_PRINT(DEBUG_TRACE,"Parameter Name is %s\n",ParamName.c_str());
            DEBUG_PRINT(DEBUG_TRACE,"Value is %s",DataParamValue[0].pParamValues);
            DEBUG_PRINT(DEBUG_TRACE," Type is %d\n",DataParamValue[0].pParamType);
            response["result"] = "SUCCESS";
            response["details"] = DataParamValue[0].pParamValues;
	    free_Memory_val(size_ret,DataParamValue);
	    return;

    }
    response["result"] = "FAILURE";
    response["details"] = "Get Param value Failure of the function";
    return;

}

/***************************************************************************
 *Function name : pam_SetParameterValues
 *Descrption    : pamPa Component Set Param Value API functionality checking
 * @param [in]  req - ParamName : Holds the name of the parameter
 * @param [in]  req - ParamValue : Holds the value of the parameter
 * @param [in]  req - Type : Holds the Type of the parameter
 * @param [out] response - filled with SUCCESS or FAILURE based on the return value
 *
 *****************************************************************************/
void pam::pam_SetParameterValues(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"Inside Function SetParamValues \n");

    int size_ret=0,i=0,setResult=0,getRet = 0;

    string ParamName=req["ParamName"].asCString();
    string ParamValue=req["ParamValue"].asCString();
    string Type=req["Type"].asCString();

    GETPARAMVALUES *DataParamValue1;

    setResult=ssp_setParameterValue(&ParamName[0],&ParamValue[0],&Type[0],1);
    if(setResult==0)
    {
        DEBUG_PRINT(DEBUG_TRACE,"Parameter Values have been set.Needs to cross be checked with Get Parameter Names\n");
        DataParamValue1=ssp_getParameterValue(&ParamName[0],&size_ret,&getRet);
    }
    else
    {
        response["result"] = "FAILURE";
        response["details"] = "FAILURE : Parameter value is not SET. Set returns failure";
	return;
    }

    if((DataParamValue1== NULL))
    {
        printf("GetParamValue funtion returns NULL as output\n");
    }
    else
    {
        if(strcmp(&ParamValue[0],&DataParamValue1[i].pParamValues[0])==0)
        {
            printf("Set has been validated successfully\n");
            free_Memory_val(size_ret,DataParamValue1);
            response["result"] = "SUCCESS";
            response["details"] = "Set has been validated successfully";
	    return;
        }
        else
        {
            free_Memory_val(size_ret,DataParamValue1);
            printf("Parameter Value has not changed after a proper Set\n");

        }
    }

    response["result"] = "FAILURE";
    response["details"] = "FAILURE : Parameter Value has not changed after a proper Set";
    return;
}

/*******************************************************************************************
 *
 * Function Name        : pam_Setparams
 * Description          : This function will invoke TDK Component SET Value wrapper
 *                        function
 *
 * @param [in] req-        This holds Path name, Value to set and its type
 * @param [out] response - filled with SUCCESS or FAILURE based on the return value of
 *                         ssp_setParameterValue
 ********************************************************************************************/

void pam::pam_Setparams(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n pam_Setparams --->Entry\n");

    int returnValue = 0;
    char ParamName[MAX_PARAM_SIZE];
    char ParamValue[MAX_PARAM_SIZE];
    char ParamType[MAX_PARAM_SIZE];

    strcpy(ParamName,req["ParamName"].asCString());
    strcpy(ParamValue,req["ParamValue"].asCString());
    strcpy(ParamType,req["Type"].asCString());

    DEBUG_PRINT(DEBUG_TRACE,"\npam_Setparams:: ParamName input is %s",ParamName);
    DEBUG_PRINT(DEBUG_TRACE,"\npam_Setparams:: ParamValue input is %s",ParamValue);
    DEBUG_PRINT(DEBUG_TRACE,"\npam_Setparams:: ParamType input is %s",ParamType);

    returnValue = ssp_setParameterValue(&ParamName[0],&ParamValue[0],&ParamType[0],1);

    if(0 == returnValue)
    {
        response["result"]="SUCCESS";
        response["details"]="Set operation success";
    }
    else
    {
        response["result"]="FAILURE";
        response["details"]="pam_Setparams:: Set operation failed";
        DEBUG_PRINT(DEBUG_TRACE,"\n pam_Set::Set Operation failed !!! \n");
        return;
    }

    DEBUG_PRINT(DEBUG_TRACE,"\n pam_Setparams --->Exit\n");
    return;
}

/*******************************************************************************************
 *
 * Function Name    : pam_CRRestart
 * Description      : This function will kill the CR process which is running by default
 *                    and check if the system has restarted after kill.
 *
 * @param [out] response - filled with SUCCESS or FAILURE based on the return value
 *
 *******************************************************************************************/

void pam::pam_CRRestart(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n pam_CRRestart --->Entry \n");

    int returnValue = 0;

    returnValue = ssp_CRRestart();
    if(0 == returnValue)
    {
        response["result"]="SUCCESS";
        response["details"]="Successfully rebooted the system after CR is killed\n";
    }
    else
    {
        response["result"]="FAILURE";
        response["details"]="Failed to reboot the system after CR being killed\n";
        DEBUG_PRINT(DEBUG_TRACE,"\n pam_CRRestart --->Exit\n");
	return;
    }
    DEBUG_PRINT(DEBUG_TRACE,"\n pam_CRRestart  --->Exit\n");
    return;

}

/**************************************************************************
 * Function Name	: CreateObject
 * Description	: This function will be used to create a new object for the
 *	                class "pam".
 *
 **************************************************************************/

extern "C" pam* CreateObject(TcpSocketServer &ptrtcpServer)
{
    return new pam(ptrtcpServer);
}

/**************************************************************************
 * Function Name : cleanup
 * Description   : This function will be used to clean the log details.
 *
 **************************************************************************/

bool pam::cleanup(IN const char* szVersion)
{
    DEBUG_PRINT(DEBUG_LOG,"pam shutting down\n");
    return TEST_SUCCESS;
}

/**************************************************************************
 * Function Name : DestroyObject
 * Description   : This function will be used to destroy the object.
 *
 **************************************************************************/
extern "C" void DestroyObject(pam *stubobj)
{
    DEBUG_PRINT(DEBUG_LOG,"Destroying pam object\n");
    delete stubobj;
}
