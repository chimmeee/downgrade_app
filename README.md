**Ví dụ với Zalo apk:**

#cd C:\platform-tools

#adb devices

#adb shell pm  path com.zing.zalo

#adb shell pm unistall -k com.zing.zalo

#adb reboot

 ++wait 30 seconds for reboot++
 
#adb devices

 ++check if the devices is connect++
 
#adb install com.zing.zalo_21.10.02.r1.apk

++wait 30second for install++ 

#adb backup -f C:\platform-tools\zalo_backup com.zing.zalo

++Nhấn màn hình đồng ý backup - file backup sẽ chứa dữ liệu chat backup của zalo++
