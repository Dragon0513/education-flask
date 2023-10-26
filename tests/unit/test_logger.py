import unittest


class TestLogger(unittest.TestCase):
    def setUp(self) -> None:
        import utils.logger as log

        self.logger = log
        self.logger.configure_dict()

    def test_logger_error(self):
        res = self.logger.error("error")
        # res to match logger.logging_config["formatters"]["default"]["format"]
        formatted_res = self.logger.logging.Formatter(
            self.logger.g_logging_config["formatters"]["default"]["format"]
        ).format(
            self.logger.logging.LogRecord(
                name=self.logger.LoggerType.DEFAULT.name,
                level=self.logger.logging.ERROR,
                pathname="",
                lineno=0,
                msg="error",
                args=(),
                exc_info=None,
            )
        )
        # replace date with static date
        res = res.replace(res[1:24], "[2023-10-25 15:41:48,786]")
        formatted_res = formatted_res.replace(
            formatted_res[1:24], "[2023-10-25 15:41:48,786]"
        )
        self.assertEqual(res, formatted_res)

    def test_logger_info(self):
        res = self.logger.info("info")
        # res to match logger.logging_config["formatters"]["default"]["format"]
        formatted_res = self.logger.logging.Formatter(
            self.logger.g_logging_config["formatters"]["default"]["format"]
        ).format(
            self.logger.logging.LogRecord(
                name=self.logger.LoggerType.DEFAULT.name,
                level=self.logger.logging.INFO,
                pathname="",
                lineno=0,
                msg="info",
                args=(),
                exc_info=None,
            )
        )
        # replace date with static date
        res = res.replace(res[1:24], "[2023-10-25 15:41:48,786]")
        formatted_res = formatted_res.replace(
            formatted_res[1:24], "[2023-10-25 15:41:48,786]"
        )
        self.assertEqual(res, formatted_res)

    def test_logger_debug(self):
        res = self.logger.debug("debug")
        # res to match logger.logging_config["formatters"]["default"]["format"]
        formatted_res = self.logger.logging.Formatter(
            self.logger.g_logging_config["formatters"]["default"]["format"]
        ).format(
            self.logger.logging.LogRecord(
                name=self.logger.LoggerType.DEFAULT.name,
                level=self.logger.logging.DEBUG,
                pathname="",
                lineno=0,
                msg="debug",
                args=(),
                exc_info=None,
            )
        )
        # replace date with static date
        res = res.replace(res[1:24], "[2023-10-25 15:41:48,786]")
        formatted_res = formatted_res.replace(
            formatted_res[1:24], "[2023-10-25 15:41:48,786]"
        )
        self.assertEqual(res, formatted_res)

    def test_logger_warn(self):
        res = self.logger.warn("warn")
        # res to match logger.logging_config["formatters"]["default"]["format"]
        formatted_res = self.logger.logging.Formatter(
            self.logger.g_logging_config["formatters"]["default"]["format"]
        ).format(
            self.logger.logging.LogRecord(
                name=self.logger.LoggerType.DEFAULT.name,
                level=self.logger.logging.WARNING,
                pathname="",
                lineno=0,
                msg="warn",
                args=(),
                exc_info=None,
            )
        )
        # replace date with static date
        res = res.replace(res[1:24], "[2023-10-25 15:41:48,786]")
        formatted_res = formatted_res.replace(
            formatted_res[1:24], "[2023-10-25 15:41:48,786]"
        )
        self.assertEqual(res, formatted_res)
