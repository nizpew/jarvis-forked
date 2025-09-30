import ollama
import asyncio

from modules.tools.sky_color import SkyColor
from modules.tools.greet_user import GreetUser
from modules.tools.get_current_weather import CurrentWeather
from modules.tools.duckduckgo_search import DuckDuckGoSearch
from modules.tools.google_search import SearchTool
from modules.tools.current_time_tool import CurrentTimeTool
from modules.tools.current_date_tool import CurrentDateTool
from modules.tools.youtube_tool import YouTubeTool
from modules.tools.battery_level_tool import BatteryLevelTool

class OllamaNLP:

    def __init__(self):
        # Instantiate tool classes
        self.sky_color = SkyColor()
        self.greet_user = GreetUser()
        self.current_weather = CurrentWeather()
        self.duckduckgo_search = DuckDuckGoSearch()
        self.search_tool = SearchTool()
        self.current_time_tool = CurrentTimeTool()
        self.current_date_tool = CurrentDateTool()
        self.youtube_tool = YouTubeTool()
        self.battery_level_tool = BatteryLevelTool()
        
        # Initialize the message history list
        self.messages = []

    def generate_text(self, model, prompt, systemPrompt=""):

        user_message = prompt
        function_result = None

        # Add system prompt once if not already added
        if not self.messages:
            if systemPrompt:
                self.messages.append({'role': 'system', 'content': systemPrompt})
            else:
                self.messages.append({
                    'role': 'system',
                    'content': 'You are Jarvis, a helpful AI assistant from the Iron Man movie. You only respond with short answers and refer to me as "Sir".'
                })

        # Trigger functions based on prompt
        if any(phrase in prompt.lower() for phrase in self.sky_color.trigger_phrases()):
            function_result = self.sky_color.get_info()
        elif any(phrase in prompt.lower() for phrase in self.greet_user.trigger_phrases()):
            function_result = self.greet_user.greet()
        elif any(phrase in prompt.lower() for phrase in self.current_weather.trigger_phrases()):
            city = prompt.split("in")[-1].strip()
            function_result = self.current_weather.get_current_weather(city)
        elif any(phrase in prompt.lower() for phrase in self.duckduckgo_search.trigger_phrases()):
            query = prompt
            for phrase in self.duckduckgo_search.trigger_phrases():
                query = query.replace(phrase, "")
            function_result = self.duckduckgo_search.duckduckgo_search(query.strip())
        elif any(phrase in prompt.lower() for phrase in self.search_tool.trigger_phrases()):
            function_result = self.search_tool.perform_search(prompt)
        elif any(phrase in prompt.lower() for phrase in self.current_time_tool.trigger_phrases()):
            function_result = self.current_time_tool.get_current_time()
        elif any(phrase in prompt.lower() for phrase in self.current_date_tool.trigger_phrases()):
            function_result = self.current_date_tool.get_current_date()
        elif any(phrase in prompt.lower() for phrase in self.youtube_tool.trigger_phrases()):
            function_result = self.youtube_tool.play_video(prompt)
        elif any(phrase in prompt.lower() for phrase in self.battery_level_tool.trigger_phrases()):
            function_result = self.battery_level_tool.get_battery_level()

        # Construct system prompt if a tool was triggered
        if function_result:
            systemPrompt = (
                f"You are restricted to this information in your response: {function_result}. "
                "Use it as context to respond accurately. Always stay within the scope of this data and do not be creative."
            )
            print("---------------------------------")
            print(f"Function call: {function_result}")
            print("---------------------------------")

        # Add system prompt as a message
        if systemPrompt:
            self.messages.append({'role': 'system', 'content': systemPrompt})

        # Add the current user prompt
        self.messages.append({'role': 'user', 'content': user_message})

        # Call Ollama
        try:
            response = ollama.chat(model=model, messages=self.messages)
            assistant_reply = response['message']['content']
            self.messages.append({'role': 'assistant', 'content': assistant_reply})
            return assistant_reply
        except Exception as e:
            error_message = f"An error occurred: {str(e)}"
            self.messages.append({'role': 'assistant', 'content': error_message})
            return error_message

