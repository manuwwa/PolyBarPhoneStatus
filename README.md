# PolyBarPhoneStatus
PolyBar Phone status using home assistant api

# Prerequisites
1. PolyBar
2. FontAvesome 
Installation in Arch :
```
yay -S ttf-font-awesome
```
3. Home assistand instance
4. Phone app for home assistant configured to send phone battery status

# Installation
1. Clone the repository
2. copy homeAssistant_default.json to homeAssistant.json and edit file:
    1. Get home assistant token and set the token value in homeAssistant.json
    2. Set home assistant url
    3. Set batery level entity id
    4. Set bater status entity id
      Example:
      ```
      {
        "homeAssistantUrl":"hassioio.hasio.hass",
        "token": "someVeryLongToken",
        "bateryLevelEntityId": "sensor.samsung_pro_phone_battery_level",
        "batteryStatusEntityyId": "sensor.samsung_pro_phone_battery_state"
      }
      ```
4. Launch the phoneStatus.py via terminal and if the output is ok continue
5. Make changes on Your polyBar configuration:

    1.Add module code:
      ```
      [module/phoneStatus]
      type = custom/script
      exec = ~/.config/polybar/phoneStatus.py
      interval = 2
      format= <label>
      ```
    3. Add module (example modules-right)
      ```
      modules-right = phoneStatus
      ```
  
6. Move pphoneStatus.py and homeAssistant.json to ~/.config/polybar/config
7. Reload polbar
