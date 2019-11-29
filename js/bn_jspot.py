from js.jsEntity import JsEntity


class bn_jspot(JsEntity):

    def __init__(self):
        JsEntity.__CONNECT_INFO()

    def get_singleton(self):
        return self
