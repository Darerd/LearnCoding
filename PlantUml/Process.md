```uml
#### 忘记密码#####
@startuml

start
:"输入邮箱";
:"输入图片验证码";
if ("邮箱是否注册或验证") then (yes)
    if ("图形验证码") then (no)
        :"提示：邮箱或验证码不正确";
        stop
    else(yes)
    endif
else(no)
    :"提示：邮箱未注册或验证";
    stop
endif
:"发送验证邮件";
:"打开重置密码链接";
:"输入新密码";

if ("密码格式符合要求") then (yes)
:"密码二次确认";
else(no)
:"提示：请输入符合要求的密码";
stop
endif
:"确定";
stop
@enduml
```

```eml
#### 注册账号#####
@startuml

start
if ("是否已有邮箱账号") then (yes)
    :"填写邮箱地址";
    else(no)
    :"进入登录页框架";
    stop
    endif
if ("邮箱是否为空") then (yes)
    :"提示：邮箱不能为空";
    stop
else(no)
    if ("邮箱是否已存在") then (yes)
        :"提示：邮箱已注册，请直接登录";
        stop
    else(no)
        if ("邮箱格式是否合法") then (no)
            :"提示：请输入正确的邮箱";
        stop
        else(yes)
            if ("邮箱是否为临时邮箱") then (yes)
            :"提示：请输入您的常用邮箱";
            stop
            else(no)
    endif
endif
:"填写密码";
if ("密码是否为空") then (yes)
    :"提示：密码不能为空";
    stop
else(no)
    if ("密码长度是否在8-32位之间") then (no)
        :"提示：密码长度需要在8-32位之间";
    stop
    else(yes)
        if ("密码是否符合字符要求") then (no)
        :"提示：请输入字母、数字和特殊符号";
        stop
        else(yes)
        endif
    endif
endif
:"输入手机号";
if ("是否为空") then (yes)
:"提示：手机号不能为空";
stop
else(no)
    if ("是否正确") then (no)
    :"提示：请输入正确的手机号";
    stop
    else(no)
    endif
endif
:"输入图形验证码";
if ("是否为空") then (yes)
:"输入框外层为红色 以做提示";
stop
else(no)
    if ("是否超时") then (yes)
    :"提示：请刷新验证码";
    note left: 用户手动刷新
    stop
    else(no)
    :"获取验证码";
    endif
endif
if ("是否勾选用户协议") then (no)
:"注册按钮不可选";
stop
else(yes)
:"注册";
endif
if ("短信验证码是否正确") then (no)
:"请输入正确的短信验证码";
    if ("是否重新获取") then (no)
    stop
    else(yes)
    :"循环不会写";
    stop
    endif
else(yes)
if ("短信验证码是否有效") then (no)
:"验证码已失效，请重新获取";
stop
else(yes)
:"注册成功";
endif
stop
@enduml
```

