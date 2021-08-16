from telebot import telegram, conf
import dolarsi

options = conf.open_env()
token = options["TELEGRAM_TOKEN"]


def get_chatid_and_Send_Dolar_Response(tkn):
    """"
    Esta funcion
    la uso para obtener el chat id de un mensaje. Esta mal hecha porque busca el indice 0, por lo tanto
    busca el update mas antiguo. Puede generar un problema y habria que buscar una funcion similar a 
    telegram.get_update_id_V2 para que obtenga el ultimo update y de ahi sacar el chat id actualizado
    """
    result_Data = telegram.get_updates(token)
    for result in result_Data:
        result_message_Data=result["message"]
        
        chat_Data=result_message_Data["chat"]
        chatid=chat_Data["id"]
        print(chatid)
        message_Info=result["message"]
        message_Text_info=message_Info["text"]
        if "dolar oficial" in message_Text_info:

        
            try:
                #chatid=chat_id.get_chatid()
                dolar=dolarsi.Dolar()
                oficial_Compra=dolar.get_oficial_Compra()
                oficial_Venta=dolar.get_oficial_Venta()
                message=f"El DOLAR OFICIAL cuesta ${oficial_Compra} para la Compra y ${oficial_Venta} para la venta"
                telegram.send_message(message, chatid, token)
            except KeyError:
                print("Problemas en la ejecucion")
        if "dolar blue" in message_Text_info:
            try:
                dolar=dolarsi.Dolar()
                blue_Compra=dolar.get_blue_Compra()
                blue_Venta=dolar.get_blue_Venta()
                message=f"El DOLAR BLUE cuesta ${blue_Compra} para la Compra y ${blue_Venta} para la venta"
                telegram.send_message(message, chatid, token)
            except KeyError:
                print("Problemas en la ejecucion")

