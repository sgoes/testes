from selenium import webdriver
import time


class WhatsappBot:
    def __init__(self):
        self.mensagem = "Isto é só um teste. Se aparecer esta mensagem, quer dizer que sei criar bots para whatsapp"
        self.grupos = ["Testes"]
        options = webdriver.ChromeOptions()
        options.add_argument('lang=pt')
        self.driver = webdriver.Chrome(executable_path=r'./chromedriver.exe')

    def EnviarMensagens(self):
        # <span dir="auto" title="Testes" class="emoji-texttt _ccCW FqYAR i0jNr">Testes</span>
        # <div tabindex="-1" class="p3_M1">
        # <span data-testid="send" data-icon="send" class="">
        print("ESTA MERDA NAO FUNCIONA")

        self.driver.get('https://web.whatsapp.com/')
        time.sleep(30)
        for grupo in self.grupos:
            grupo = self.driver.find_element_by_xpath(
                f"//span[@title='{grupo}']")
            time.sleep(3)
            grupo.click()
            chat_box = self.driver.find_element_by_class_name('p3_M1')
            time.sleep(3)
            chat_box.click()
            chat_box.send_keys(self.mensagem)
            botao_enviar = self.driver.find_element_by_xpath(
                "//span[@data-icon='send']")
            time.sleep(3)
            botao_enviar.click()
            time.sleep(5)


bot = WhatsappBot()
bot.EnviarMensagens()
