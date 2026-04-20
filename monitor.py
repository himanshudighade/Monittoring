import psutil
import platform
import time

def get_system_health():
    boot_time = psutil.boot_time()
    uptime = int(time.time() - boot_time)

    try:
        disk = psutil.disk_usage('C:').percent
    except:
        disk = 0

    try:
        temps = psutil.sensors_temperatures()
        cpu_temp = temps['coretemp'][0].current if 'coretemp' in temps else None
    except:
        cpu_temp = None

    data = {
        "cpu": psutil.cpu_percent(interval=1),
        "memory": psutil.virtual_memory().percent,
        "disk": disk,
        "processes": len(psutil.pids()),

        "net_sent": round(psutil.net_io_counters().bytes_sent / (1024 * 1024), 2),
        "net_recv": round(psutil.net_io_counters().bytes_recv / (1024 * 1024), 2),

        "uptime": uptime,
        "system": platform.system(),
        "cpu_temp": cpu_temp
    }

    return data     