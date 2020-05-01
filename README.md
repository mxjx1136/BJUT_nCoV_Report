# nCoVReport

基于 Python3 的适用于北工大的 nCoV 自动填报脚本

[下载地址](https://github.com/nonPointer/BJUT_nCoV_Report/releases)

## 使用方式

1. 创建 `account.txt`，格式为（不包含方括号）
    ```text
    [学号]
    [密码]
    ```
2. 修改 `main.py` 内的经纬度和地址信息（可选)
3. 安装所需依赖：`pip3 install -r requirements.txt`
4. 执行 `main.py`

## 自动化

### Linux：使用 Crontab

每天早晨 8:00 上报并在 8:01、9:00、9:01 重试。
```shell script
0,1 8,9 * * * python3 main.py
```

### Windows：使用计划任务（Task Scheduler）

务必选中 `Run whether user is logged on or not`。
