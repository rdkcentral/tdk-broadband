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


#ifndef __SSP_PAM_BRIDGE_C__
#define __SSP_PAM_BRIDGE_C__

//#include "ssp_global.h"
//#include "ccsp_dm_api.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
//#include <sys/types.h>
//#include <sys/socket.h>
//#include <netinet/in.h>
//#include <netdb.h>
//#include "pthread.h"
//#include "ssp_tdk_wrp.h"
//#include <pthread.h>
//#include <ccsp_message_bus.h>
//#include <ccsp_base_api.h>
//#include <sys/time.h>
//#include <time.h>
//#include <signal.h>
//#include "ccsp_memory.h"
//#include <ccsp_custom.h>
//#include <dslh_definitions_database.h>
//#include <sys/ucontext.h>

//#include "cosa_apis.h"
//#include "cosa_dml_api_common.h"
//#include "cosa_dhcpv4_apis.h"
//#include "cosa_dml_api_dns.h"
//#include "cosa_bridging_dml.h"
//#include "cosa_x_cisco_com_multilan_apis.h"
//#include "cosa_ethernet_apis_multilan.h"
//#include "cosa_upnp_apis.h"

//#define SSP_SUCCESS       0

//#define SSP_FAILURE       1


/*******************************************************************************************
 *
 * Function Name        : ssp_CRRestart
 * Description          : This function will kill the CR process which is running by default
 *                        and check if the system has rebooted after kill.
 *
 * @param [out]         : return status an integer value 0-success and 1-Failure
 ********************************************************************************************/

int ssp_CRRestart()
{
    printf("\n Entering ssp_CRRestart function\n\n");

    if(0 == system("pidof CcspCrSsp > /dev/null"))  {
        printf("\nCR is running\n");
        printf("\nGoing to kill CR process\n");
        system ("kill -9 `pidof CcspCrSsp`");
        sleep(1800);

        if(0 == system("pidof CcspCrSsp > /dev/null"))   {
            printf("\nCcspCrSsp process has restarted \n");
            return 0;

        }

        else
        {
            printf ("\nCcspCrSsp process is not restarted after kill\n");
            return 1;
        }
    }

    else {

        printf ("\nCcspCrSsp process is not running\n");
        return 1;
    }
    printf("\n Exiting ssp_CRRestart function\n\n");

}
