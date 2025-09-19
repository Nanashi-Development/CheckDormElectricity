# CheckDormElectricity

- 由于没有检查电费是否充裕的习惯（看一眼还有多少度的操作过于繁琐），导致寝室存在突然断电的情况，故编写本程序。
- 使用本项目需要抓包基础。 👉[学习如何使用微信调试抓包](./PacketCapture.md)
- 本项目为浙江万里学院（ZWU），其他学校若使用相同缴费系统（jkschool.lsmart.cn）可尝试进行适配。
- 本项目用于自动查询宿舍房间和空调房间的电量，并通过钉钉机器人发送提醒。

## 功能简介

- 可通过青龙面板定时运行
- 查询指定房间的电量信息
- 电量低于阈值时自动通过钉钉机器人强提醒，否则为弱提醒（表现为无声通知）

## 使用方法

1. **安装依赖**

   ```sh
   pip install -r requirements.txt
   ```

   若使用青龙面板运行请自行安装依赖

2. **配置参数**

   - 编辑 `main.py`，填写你的钉钉机器人 `webhook` 和 `secret`，以及房间参数（详见房间说明）。

3. **运行脚本**

   ```sh
   python main.py
   ```
   若使用青龙面板运行请自行创建任务（命令为 **task PATH_TO_YOUR_FILE**）

## 房间说明
   ```python
   Room = {
    'openId':'None',  # 保持None即可
    'wxArea':'',  # 未知
    'areaNo':'',  # 校区ID
    'buildNo':'',  # 楼号ID
    'roomNo':'',  # 寝室ID
   }
   ```
   - **data_studentRoom** 中请填写学生房间参数
   - **data_airConditionerRoom** 中请填写空调房间参数