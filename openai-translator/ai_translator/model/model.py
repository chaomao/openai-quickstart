from book import ContentType


class Model:
    @staticmethod
    def make_text_prompt(text: str, target_language: str) -> str:
        return f"翻译为{target_language}, 请保持原来的格式：\n{text}"

    @staticmethod
    def make_table_prompt(table: str, target_language: str) -> str:
        return f"将下面所有内容翻译为{target_language}，保持间距（空格，分隔符），以表格形式返回, 注意不要以 markdown 形式返回，表格头部和表格内容都翻译成中文：\n{table}"

    def translate_prompt(self, content, target_language: str) -> str:
        if content.content_type == ContentType.TEXT:
            return self.make_text_prompt(content.original, target_language)
        elif content.content_type == ContentType.TABLE:
            return self.make_table_prompt(content.get_original_as_str(), target_language)

    def make_request(self, prompt):
        raise NotImplementedError("子类必须实现 make_request 方法")
