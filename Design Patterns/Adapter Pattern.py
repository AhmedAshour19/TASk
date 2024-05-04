class ModernNotificationService:
    def send_notification(self, message):
        print(f"Sending modern notification: {message}")

class LegacySMSService:
    def send_sms(self, text):
        print(f"Sending SMS: {text}")

class SMSAdapter(ModernNotificationService):
    def __init__(self, legacy_sms_service):
        self.legacy_sms_service = legacy_sms_service

    def send_notification(self, message):
        self.legacy_sms_service.send_sms(message)

# Client code
if __name__ == "__main__":
    modern_notification = ModernNotificationService()
    legacy_sms = LegacySMSService()
    sms_adapter = SMSAdapter(legacy_sms)

    modern_notification.send_notification("Hello, modern world!")
    sms_adapter.send_notification("Hello, legacy system!")
