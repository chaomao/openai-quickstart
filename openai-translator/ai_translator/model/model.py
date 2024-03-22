from book import ContentType


class Model:
    @staticmethod
    def make_text_prompt(text: str, target_language: str) -> str:
        if target_language == "中文":
            return f"翻译为{target_language}, 请保持原来的格式：\n{text}"
        elif target_language == "西班牙文":
            return f"Traducido al español, por favor conserve el formato original: \n{text}"
        else:
            raise NotImplementedError(f"暂不支持翻译为 {target_language}")

    @staticmethod
    def make_table_prompt(table: str, target_language: str) -> str:
        if target_language == "中文":
            return f"将下面所有内容翻译为{target_language}，保持间距（空格，分隔符），以表格形式返回, 注意不要以 markdown 形式返回，表格头部和表格内容都翻译成中文：\n{table}"
        elif target_language == "西班牙文":
            return f"Traduzca todo el contenido siguiente al español, mantenga los espacios (espacios, separadores) y devuélvalo en forma de tabla. Tenga cuidado de no devolverlo en forma de rebajas. El encabezado y el contenido de la tabla están traducidos al chino:\ n{table}"
        else:
            raise NotImplementedError(f"暂不支持翻译为 {target_language}")

    def translate_prompt(self, content, target_language: str) -> str:
        if content.content_type == ContentType.TEXT:
            return self.make_text_prompt(content.original, target_language)
        elif content.content_type == ContentType.TABLE:
            return self.make_table_prompt(content.get_original_as_str(), target_language)

    def make_request(self, prompt):
        raise NotImplementedError("子类必须实现 make_request 方法")
