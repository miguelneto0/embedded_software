#define TARGET_TEMP = [50, 65, 80] 
#define TARGET_RPM  = [20, 30, 40] 
#define TARGET_TIME = [1800, 1800, 3600]

int phase = 0;
int rpm = 0;
double temp = 0;

int activate_rotation(){ return rpm++; }
int activate_rotation(){ return temp++; }
void update_targets(){ phase++; }

function control_process():

    current_temp = 0
    current_rpm  = 0
    current_time = 0
    
    start_time = 0
    target_reached = False
    
    while ( !target_reached ) {
        current_rpm  = activate_rotation()
        current_temp = activate_heater()
        if (current_rpm != TARGET_RPM[phase] and current_temp != TARGET_TEMP[phase]){
            start_time = timer.getCurrentTime()
        }
    }

    while (current_time != target_time[phase]) {
        current_time = timer.getTick()
        if (current_time == target_time[phase] ) {
            update_targets()                
        }
    }

function main():
    if ( phase > TARGET_RPM.size )
        return
    else {
        control_process()
    }

