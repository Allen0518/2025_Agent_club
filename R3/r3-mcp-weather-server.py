import os
from dotenv import load_dotenv
from mcp.server.fastmcp import FastMCP

import datetime
# fastmcp docs: https://gofastmcp.com/deployment/running-server

mcp = FastMCP("", "R3WeatherServer")

@mcp.tool()
def get_weather(location: str, date: str = None) -> str:
    """查詢指定地點與日期的天氣。location 是地點，date 是日期（YYYY-MM-DD，可選）"""
    if not date:
        date = (datetime.date.today() + datetime.timedelta(days=1)).isoformat()
    return f"{location} 在 {date} 的天氣是晴時多雲，氣溫約 26~32 °C。"

if __name__ == "__main__":
    # cmd: mcp install r3-mcp-weather-server.py 即可部署到 claude 上
    mcp.run(transport="stdio")
    
# sqlite mcp server link: https://mcp.so/server/mcp_sqlite_poc/madhavarora1988?tab=content