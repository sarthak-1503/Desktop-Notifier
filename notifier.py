from plyer import notification

title = 'WhatsApp Message from College Group'
message= 'College Trip, Yayy!'

notification.notify(title=title, message=message, app_icon = None, timeout=20, toast=False)
