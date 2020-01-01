# display-setter
此工具用来查询以及设置显示器分辨率，刷新率，旋转布局等信息  

## 安装方式  
>> pip install display-setter  

## Sample
```
import displaysetter
import copy
display=displaysetter.DISPLAY()
display.get_device_display_info()
print(display.display_device_info_list)
default_mode=display.get_current_mode('\\\\.\\DISPLAY4')
print(default_mode)
temp_mode=copy.deepcopy(default_mode)
temp_mode[1]=768
temp_mode[2]=1024
#define DMDO_DEFAULT    0
#define DMDO_90         1
#define DMDO_180        2
#define DMDO_270        3
temp_mode[6]=3
print(display.change_resolution(*temp_mode))
input()
print(display.change_resolution(*default_mode))
```

