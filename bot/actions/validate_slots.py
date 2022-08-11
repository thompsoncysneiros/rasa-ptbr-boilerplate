import re
import mysql.connector
from datetime import datetime
from typing import Text, List, Any, Dict

from rasa_sdk import Tracker, FormValidationAction, Action
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict
from rasa_sdk.events import AllSlotsReset


class ActionResetAllSlots(Action):

    def name(self):
        return "action_reset_all_slots"

    def run(self, dispatcher, tracker, domain):
        return [AllSlotsReset()]


class ValidateCisamForm(FormValidationAction):
    def name(self) -> Text:
        return "validate_cisam_form"

    def validate_user_lgpd(
            self,
            slot_value: Any,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate user_lgpd"""

        # listed_options = ['1', '2']

        if slot_value == '1':
            dispatcher.utter_message(response="utter_user_lgpd_sim")
            dispatcher.utter_message(response="utter_cenario_um_menu")
            return {"user_lgpd": slot_value}
        elif slot_value == '2':
            dispatcher.utter_message(response="utter_user_lgpd_nao")
            return {"user_lgpd": None, "requested_slot": None}
        else:
            dispatcher.utter_message(response="utter_user_lgpd_errado")
            return {"user_lgpd": None}

    def validate_cenario_um_menu(
            self,
            slot_value: Any,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate cenario_um_menu"""

        if slot_value == '#':
            dispatcher.utter_message(response="utter_cenario_um_menu")
            return {"cenario_um_menu": None, "user_lgpd": None}
        elif slot_value == '1':
            dispatcher.utter_message(response="utter_cenario_um_menu_resp_um")
            dispatcher.utter_message(response="utter_user_logado_nome")
            return {"cenario_um_menu": slot_value}
        elif slot_value == '2':
            dispatcher.utter_message(response="utter_cenario_um_menu_resp_dois")
            return {"cenario_um_menu": None, "user_lgpd": None, "requested_slot": None}
        else:
            dispatcher.utter_message(response="utter_cenario_um_menu_resp_errado")
            return {"cenario_um_menu": None}

    def validate_user_logado_nome(
            self,
            slot_value: Any,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate user_logado_nome"""

        if slot_value == '#':
            dispatcher.utter_message(response="utter_cenario_um_menu")
            return {"cenario_um_menu": None, "user_logado_nome": None}
        else:
            if len(slot_value) >= 2 and not slot_value.isdigit():
                dispatcher.utter_message(response="utter_user_prontuario")
                return {"user_logado_nome": slot_value}
            else:
                dispatcher.utter_message(response="utter_user_logado_nome_invalido")
                return {"user_logado_nome": None}

    def validate_user_prontuario(
            self,
            slot_value: Any,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate user_prontuario"""

        if slot_value == '#':
            return {"user_logado_nome": None, "user_prontuario": None}
        else:
            if len(slot_value) >= 2 and slot_value.isdigit():
                dispatcher.utter_message(response="utter_cenario_dois_menu")
                return {"user_prontuario": slot_value}
            else:
                dispatcher.utter_message(response="utter_user_prontuario_invalido")
                return {"user_prontuario": None}

#     def validate_cenario_dois_menu(
#             self,
#             slot_value: Any,
#             dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: DomainDict,
#     ) -> Dict[Text, Any]:
#         """Validate cenario_dois_menu"""
#
#         if slot_value == '#':
#             return {"cenario_dois_menu": None, "user_prontuario": None}
#         elif slot_value == '1':
#             dispatcher.utter_message(response="utter_cenario_dois_menu_resp_um")
#             return {"cenario_dois_menu": slot_value}
#         elif slot_value == '2':
#             dispatcher.utter_message(response="utter_cenario_dois_menu_resp_dois")
#             return {"cenario_dois_menu": slot_value}
#         elif slot_value == '3':
#             dispatcher.utter_message(response="utter_cenario_dois_menu_resp_tres")
#             return {"cenario_dois_menu": slot_value}
#         elif slot_value == '4':
#             dispatcher.utter_message(response="utter_cenario_dois_menu_resp_quatro")
#             dispatcher.utter_message(response="utter_user_nome_paciente")
#             return {"cenario_dois_menu": slot_value}
#         else:
#             dispatcher.utter_message(response="utter_cenario_dois_menu_resp_errado")
#             return {"cenario_dois_menu": None}
#
#     def validate_user_nome_paciente(
#             self,
#             slot_value: Any,
#             dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: DomainDict,
#     ) -> Dict[Text, Any]:
#         """Validate user_nome_paciente"""
#         comparar = tracker.get_slot("cenario_dois_menu")
#
#         # Retornar cenario_dois_menu
#         if slot_value == '#':
#             dispatcher.utter_message(response="utter_cenario_dois_menu")
#             return {"user_nome_paciente": None, "cenario_dois_menu": None}
#         # Prosseguir para user_nome_paciente
#         elif comparar == '4':
#             # validador
#             if len(slot_value) <= 3 or slot_value.isdigit():
#                 dispatcher.utter_message(response="utter_user_nome_paciente_invalido")
#                 return {"user_nome_paciente": None}
#             else:
#                 dispatcher.utter_message(response="utter_user_nome_social")
#                 return {"user_nome_paciente": slot_value}
#         else:
#             dispatcher.utter_message(response="utter_cenario_dois_resp_errada_voltar")
#             return {"user_nome_paciente": None}
#
#     def validate_user_nome_social(
#             self,
#             slot_value: Any,
#             dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: DomainDict,
#     ) -> Dict[Text, Any]:
#         """Validate user_nome_social"""
#         if slot_value == '#':
#             return {"user_nome_paciente": None, "user_nome_social": None}
#         else:
#             if len(slot_value) >= 2 and not slot_value.isdigit():
#                 dispatcher.utter_message(response="utter_user_telefone")
#                 return {"user_nome_social": slot_value}
#             else:
#                 dispatcher.utter_message(response="utter_user_nome_social_invalido")
#                 return {"user_nome_social": None}
#
#     def validate_user_telefone(
#             self,
#             slot_value: Any,
#             dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: DomainDict,
#     ) -> Dict[Text, Any]:
#         """Validate user_telefone"""
#
#         if slot_value == '#':
#             return {"user_telefone": None, "user_nome_social": None}
#         else:
#             if UtilsForm.check_telefone(slot_value) == 'valido':
#                 dispatcher.utter_message(response="utter_user_data_nasc")
#                 return {"user_telefone": slot_value}
#             else:
#                 dispatcher.utter_message(response="utter_user_telefone_invalido")
#                 return {"user_telefone": None}
#
#     def validate_user_data_nasc(
#             self,
#             slot_value: Any,
#             dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: DomainDict,
#     ) -> Dict[Text, Any]:
#         """Validate user_data_nasc"""
#
#         if slot_value == '#':
#             return {"user_data_nasc": None, "user_telefone": None}
#         else:
#             if UtilsForm.check_data_nasc(slot_value) == 'valido':
#                 dispatcher.utter_message(response="utter_user_sexo")
#                 return {"user_data_nasc": slot_value}
#             else:
#                 dispatcher.utter_message(response="utter_user_data_nasc_invalido")
#                 return {"user_data_nasc": None}
#
#     def validate_user_sexo(
#             self,
#             slot_value: Any,
#             dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: DomainDict,
#     ) -> Dict[Text, Any]:
#         """Validate user_sexo"""
#
#         if slot_value == '#':
#             return {"user_sexo": None, "user_data_nasc": None}
#         else:
#             if slot_value.upper() == 'M' or slot_value.upper() == 'F':
#                 dispatcher.utter_message(response="utter_user_cpf")
#                 return {"user_sexo": slot_value}
#             else:
#                 dispatcher.utter_message(response="utter_user_sexo_invalido")
#                 return {"user_sexo": None}
#
#     def validate_user_cpf(
#             self,
#             slot_value: Any,
#             dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: DomainDict,
#     ) -> Dict[Text, Any]:
#         """Validate user_cpf"""
#
#         if slot_value == '#':
#             return {"user_cpf": None, "user_sexo": None}
#         else:
#             if UtilsForm.check_cpf(slot_value) == "valido":
#                 dispatcher.utter_message(response="utter_user_nome_mae")
#                 return {"user_cpf": slot_value}
#             else:
#                 dispatcher.utter_message(response="utter_user_cpf_invalido")
#                 return {"user_cpf": None}
#
#     def validate_user_nome_mae(
#             self,
#             slot_value: Any,
#             dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: DomainDict,
#     ) -> Dict[Text, Any]:
#         """Validate user_nome_mae"""
#
#         if slot_value == '#':
#             return {"user_nome_mae": None, "user_cpf": None}
#         else:
#             if len(slot_value) >= 3 and not slot_value.isdigit():
#                 dispatcher.utter_message(response="utter_user_email")
#                 return {"user_nome_mae": slot_value}
#             else:
#                 dispatcher.utter_message(response="utter_user_nome_mae_invalido")
#                 return {"user_nome_mae": None}
#
#     def validate_user_email(
#             self,
#             slot_value: Any,
#             dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: DomainDict,
#     ) -> Dict[Text, Any]:
#         """Validate user_email"""
#
#         if slot_value == '#':
#             return {"user_email": None, "user_nome_mae": None}
#         else:
#             if UtilsForm.check_email(slot_value) == 'valido':
#                 dispatcher.utter_message(response="utter_user_end_cep")
#                 return {"user_email": slot_value}
#             else:
#                 dispatcher.utter_message(response="utter_user_email_invalido")
#                 return {"user_email": None}
#
#     def validate_user_end_cep(
#             self,
#             slot_value: Any,
#             dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: DomainDict,
#     ) -> Dict[Text, Any]:
#         """Validate user_end_cep"""
#
#         if slot_value == '#':
#             return {"user_end_cep": None, "user_email": None}
#         else:
#             if UtilsForm.check_cep(slot_value) == 'valido':
#                 dispatcher.utter_message(response="utter_user_end_rua")
#                 return {"user_end_cep": slot_value}
#             else:
#                 dispatcher.utter_message(response="utter_user_end_cep_invalido")
#                 return {"user_end_cep": None}
#
#     def validate_user_end_rua(
#             self,
#             slot_value: Any,
#             dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: DomainDict,
#     ) -> Dict[Text, Any]:
#         """Validate user_end_rua"""
#
#         if slot_value == '#':
#             return {"user_end_cep": None, "user_end_rua": None}
#         else:
#             if len(slot_value) >= 3 and not slot_value.isdigit():
#                 dispatcher.utter_message(response="utter_user_end_numero")
#                 return {"user_end_rua": slot_value}
#             else:
#                 dispatcher.utter_message(response="utter_user_end_rua_invalido")
#                 return {"user_end_rua": None}
#
#     def validate_user_end_numero(
#             self,
#             slot_value: Any,
#             dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: DomainDict,
#     ) -> Dict[Text, Any]:
#         """Validate user_end_numero"""
#
#         if slot_value == '#':
#             return {"user_end_rua": None, "user_end_numero": None}
#         else:
#             if slot_value.isdigit():
#                 dispatcher.utter_message(response="utter_user_end_complemento")
#                 return {"user_end_numero": slot_value}
#             else:
#                 dispatcher.utter_message(response="utter_user_end_numero_invalido")
#                 return {"user_end_numero": None}
#
#     def validate_user_end_complemento(
#             self,
#             slot_value: Any,
#             dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: DomainDict,
#     ) -> Dict[Text, Any]:
#         """Validate user_end_complemento"""
#
#         if slot_value == '#':
#             return {"user_end_numero": None, "user_end_complemento": None}
#         else:
#             if len(slot_value) >= 3:
#                 dispatcher.utter_message(response="utter_user_end_bairro")
#                 return {"user_end_complemento": slot_value}
#             else:
#                 dispatcher.utter_message(response="utter_user_end_complemento_invalido")
#                 return {"user_end_complemento": None}
#
#     def validate_user_end_bairro(
#             self,
#             slot_value: Any,
#             dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: DomainDict,
#     ) -> Dict[Text, Any]:
#         """Validate user_end_bairro"""
#
#         if slot_value == '#':
#             return {"user_end_bairro": None, "user_end_complemento": None}
#         else:
#             if len(slot_value) >= 3 and not slot_value.isdigit():
#                 dispatcher.utter_message(response="utter_user_end_cidade")
#                 return {"user_end_bairro": slot_value}
#             else:
#                 dispatcher.utter_message(response="utter_user_end_bairro_invalido")
#                 return {"user_end_bairro": None}
#
#     def validate_user_end_cidade(
#             self,
#             slot_value: Any,
#             dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: DomainDict,
#     ) -> Dict[Text, Any]:
#         """Validate user_end_cidade"""
#
#         if slot_value == '#':
#             return {"user_end_cidade": None, "user_end_bairro": None}
#         else:
#             if len(slot_value) >= 3 and not slot_value.isdigit():
#                 dispatcher.utter_message(response="utter_user_end_uf")
#                 return {"user_end_cidade": slot_value}
#             else:
#                 dispatcher.utter_message(response="utter_user_end_cidade_invalido")
#                 return {"user_end_cidade": None}
#
#     def validate_user_end_uf(
#             self,
#             slot_value: Any,
#             dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: DomainDict,
#     ) -> Dict[Text, Any]:
#         """Validate_user_end_uf"""
#
#         if slot_value == '#':
#             return {"user_end_uf": None, "user_end_cidade": None}
#         else:
#             if UtilsForm.check_uf(slot_value.upper()) == 'valido':
#                 dispatcher.utter_message(response="utter_user_numero_sus")
#                 return {"user_end_uf": slot_value}
#             else:
#                 dispatcher.utter_message(response="utter_user_end_uf_invalido")
#                 return {"user_end_uf": None}
#
#     def validate_user_numero_sus(
#             self,
#             slot_value: Any,
#             dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: DomainDict,
#     ) -> Dict[Text, Any]:
#         """Validate user_numero_sus"""
#
#         if slot_value == '#':
#             return {"user_numero_sus": None, "user_end_uf": None}
#         else:
#             if len(slot_value) == 15 and slot_value.isdigit():
#                 dispatcher.utter_message(response="utter_user_certidao_nascimento")
#                 return {"user_numero_sus": slot_value}
#             else:
#                 dispatcher.utter_message(response="utter_user_numero_sus_invalido")
#                 return {"user_numero_sus": None}
#
#     def validate_user_certidao_nascimento(
#             self,
#             slot_value: Any,
#             dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: DomainDict,
#     ) -> Dict[Text, Any]:
#         """Validate user_certidao_nascimento"""
#
#         if slot_value == '#':
#             return {"user_certidao_nascimento": None, "user_numero_sus": None}
#         else:
#             if (
#                     len(slot_value) >= 3 and slot_value.isdigit()) or slot_value.upper() == 'NÃO' or slot_value.upper() == 'NAO':
#                 dispatcher.utter_message(response="utter_user_certidao_casamento")
#                 return {"user_certidao_nascimento": slot_value}
#             else:
#                 dispatcher.utter_message(response="utter_user_certidao_nascimento_invalido")
#                 return {"user_certidao_nascimento": None}
#
#     def validate_user_certidao_casamento(
#             self,
#             slot_value: Any,
#             dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: DomainDict,
#     ) -> Dict[Text, Any]:
#         """Validate user_certidao_casamento"""
#
#         if slot_value == '#':
#             return {"user_certidao_casamento": None, "user_certidao_nascimento": None}
#         else:
#             if (
#                     len(slot_value) >= 3 and slot_value.isdigit()) or slot_value.upper() == 'NÃO' or slot_value.upper() == 'NAO':
#                 dispatcher.utter_message(response="utter_despedir")
#                 return {"user_certidao_casamento": slot_value}
#             else:
#                 dispatcher.utter_message(response="utter_user_certidao_casamento_invalido")
#                 return {"user_certidao_casamento": None}
#
#
# class UtilsForm:
#
#     def check_email(email):
#         regex = '^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$'
#         if re.search(regex, email):
#             return "valido"
#         else:
#             return "invalido"
#
#     def check_telefone(telefone):
#         regex = '^(?:[14689][1-9]|2[12478]|3[1234578]|5[1345]|7[134579])\-? ?(?:[2-8]|9[1-9])[0-9]{3}\-?[0-9]{4}$'
#         if re.search(regex, telefone):
#             return "valido"
#         else:
#             return "invalido"
#
#     def check_data_nasc(data_nasc):
#         formatos = ('%d.%m.%Y', '%d-%m-%Y', '%d/%m/%Y')
#
#         for formato in formatos:
#             try:
#                 datetime.strptime(data_nasc, formato)
#                 return "valido"
#             except ValueError:
#                 pass
#         return "invalido"
#
#     def check_cpf(cpf):
#         regex = '^(\d{3})\.?(\d{3})\.?(\d{3})\-?(\d{2})$'
#         if re.search(regex, cpf):
#             return "valido"
#         else:
#             return "invalido"
#
#     def check_cep(cep):
#         regex = '(^[0-9]{5})-?([0-9]{3}$)'
#         if re.search(regex, cep):
#             return "valido"
#         else:
#             return "invalido"
#
#     def check_uf(uf):
#         estados = (
#             "AC", "AL", "AP", "AM", "BA", "CE", "DF", "ES", "GO", "MA", "MT", "MS", "MG", "PA", "PB", "PR", "PE", "PI",
#             "RJ", "RN", "RS", "RO", "RR", "SC", "SP", "SE", "TO")
#         for estado in estados:
#             if estado == uf:
#                 return "valido"
#             else:
#                 continue
#         return "invalido"
#
#
# def DataUpdate(a, b, c, d, e, f, g, h, i, j, la, m, n, o, p, q, r, s, t, u):
#     mydb = mysql.connector.connect(
#         host="127.0.0.1",
#         port="3306",
#         user="root",
#         password="root",
#         database="Cisam"
#     )
#
#     mycursor = mydb.cursor()
#
#     sql = 'INSERT INTO UserCisam (user_lgpd, user_prontuario, user_nome_paciente, user_nome_social, user_telefone, user_data_nasc, ' \
#           'user_sexo, user_cpf, user_nome_mae, user_email, user_end_cep, ' \
#           'user_end_rua, user_end_numero, user_end_complemento, user_end_bairro, user_end_cidade, user_end_uf, ' \
#           'user_numero_sus, user_certidao_nascimento, user_certidao_casamento) VALUES ("{0}","{1}","{2}","{3}","{4}","{5}",' \
#           '"{6}","{7}","{8}","{9}","{10}","{11}","{12}","{13}","{14}","{15}","{16}","{17}","{18}","{19}");'.format(a, b, c, d, e, f, g, h, i, j, la, m, n, o, p, q, r, s, t, u)
#     mycursor.execute(sql)
#     mydb.commit()
#
#
# class ActionSubmit(Action):
#
#     def name(self) -> Text:
#         return "action_submit"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#         a = tracker.get_slot("user_lgpd")
#         b = tracker.get_slot("user_prontuario")
#         c = tracker.get_slot("user_nome_paciente")
#         d = tracker.get_slot("user_nome_social")
#         e = tracker.get_slot("user_telefone")
#         f = tracker.get_slot("user_data_nasc")
#         g = tracker.get_slot("user_sexo")
#         h = tracker.get_slot("user_cpf")
#         i = tracker.get_slot("user_nome_mae")
#         j = tracker.get_slot("user_email")
#         la = tracker.get_slot("user_end_cep")
#         m = tracker.get_slot("user_end_rua")
#         n = tracker.get_slot("user_end_numero")
#         o = tracker.get_slot("user_end_complemento")
#         p = tracker.get_slot("user_end_bairro")
#         q = tracker.get_slot("user_end_cidade")
#         r = tracker.get_slot("user_end_uf")
#         s = tracker.get_slot("user_numero_sus")
#         t = tracker.get_slot("user_certidao_nascimento")
#         u = tracker.get_slot("user_certidao_casamento")
#
#         DataUpdate(a, b, c, d, e, f, g, h, i, j, la, m, n, o, p, q, r, s, t, u)
#         return []
#

def DataUpdate(a, b):

    mydb = mysql.connector.connect(
        host='mysqldb',
        user="root",
        password="root",
        database="Cisam"
    )

    mycursor = mydb.cursor()

    sql = 'INSERT INTO UserCisam (user_lgpd, user_prontuario) VALUES ("{0}","{1}");'.format(a, b)
    mycursor.execute(sql)
    mydb.commit()
    mydb.close()


class ActionSubmit(Action):

    def name(self) -> Text:
        return "action_submit"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Enviando para o DB")
        a = tracker.get_slot("user_lgpd")
        b = tracker.get_slot("user_prontuario")

        DataUpdate(a, b)
        return []

