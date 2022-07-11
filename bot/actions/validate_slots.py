from pkgutil import extend_path
from typing import Text, List, Any, Dict

from rasa_sdk import Tracker, FormValidationAction
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict


class ValidateConsultaForm(FormValidationAction):
    def name(self) -> Text:
        return "validate_consulta_form"

    def validate_tipo_consulta(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate tipo_consulta"""

        tipo_consulta = slot_value

        if tipo_consulta.isdigit():
            tipo_consulta = int(tipo_consulta)
            if tipo_consulta > 0 and tipo_consulta <= 3:
                # validation succeeded
                return {"tipo_consulta": tipo_consulta}
        # validation failed
        dispatcher.utter_message(response="utter_tipo_consulta_errado")
        return {"tipo_consulta": None}

        #if slot_value.lower() in self.cuisine_db():
        #    # validation succeeded, set the value of the "cuisine" slot to value
        #    return {"cuisine": slot_value}
        #else:
        #    # validation failed, set this slot to None so that the
        #    # user will be asked for the slot again
        #    return {"cuisine": None}
class ValidateCisamForm(FormValidationAction):
    def name(self) -> Text:
        return "validate_cisam_form"
    
    def set_slots_none(
            self,
            slot_value: Any,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Zerar os Slots Cenário 2"""
        slot_name = tracker.get_slot("data_cenario_dois_menu")

        return {"cenario_dois_menu": slot_name, "user_nome_paciente": None, "user_nome_social": None, "user_telefone": None, "user_data_nasc": None,"user_sexo": None, "user_cpf": None, "user_nome_mae": None, "user_email": None, "user_end_cep": None, "user_end_rua": None, "user_end_numero": None, "user_end_complemento": None, "user_end_bairro": None, "user_end_cidade": None, "user_numero_sus": None, "user_certidao_nascimento": None}
    
    def validate_user_lgpd(
            self,
            slot_value: Any,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate user_lgpd"""

        data_user_lgpd = slot_value
        if data_user_lgpd == '1':
            dispatcher.utter_message(response="utter_user_lgpd_sim")
            return {"user_lgpd": data_user_lgpd}
        elif data_user_lgpd == '2':
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

        data_cenario_um_menu = slot_value
        if data_cenario_um_menu == '1':
            dispatcher.utter_message(response="utter_cenario_um_menu_resp_um")
            return {"cenario_um_menu": data_cenario_um_menu}
        elif data_cenario_um_menu == '2':
            dispatcher.utter_message(response="utter_cenario_um_menu_resp_dois")
            return {"requested_slot": None}
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

        data_user_logado_nome = slot_value
        if data_user_logado_nome == '#':
            return {"cenario_um_menu": None, "user_logado_nome": None}
        else:
            return {"user_logado_nome": data_user_logado_nome}
        
    def validate_user_prontuario(
            self,
            slot_value: Any,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate user_prontuario"""

        data_user_prontuario = slot_value
        if data_user_prontuario == '#':
            return {"user_logado_nome": None, "user_prontuario": None}
        else:
            return {"user_prontuario": data_user_prontuario}

    def validate_cenario_dois_menu(
            self,
            slot_value: Any,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate cenario_dois_menu"""

        data_cenario_dois_menu = slot_value
        if data_cenario_dois_menu == '1':
            dispatcher.utter_message(response="utter_cenario_dois_menu_resp_um")
            return {"cenario_dois_menu": data_cenario_dois_menu}
        elif data_cenario_dois_menu == '2':
            dispatcher.utter_message(response="utter_cenario_dois_menu_resp_dois")
            return {"cenario_dois_menu": data_cenario_dois_menu}
        elif data_cenario_dois_menu == '3':
            dispatcher.utter_message(response="utter_cenario_dois_menu_resp_tres")
            return {"cenario_dois_menu": data_cenario_dois_menu}
        elif data_cenario_dois_menu == '4':
            dispatcher.utter_message(response="utter_cenario_dois_menu_resp_quatro")
            dispatcher.utter_message(response="utter_user_nome_paciente")
            return {"cenario_dois_menu": data_cenario_dois_menu}
        else:
            dispatcher.utter_message(response="utter_cenario_dois_menu_resp_errado")
            return {"cenario_dois_menu": None}  


    def validate_user_nome_paciente(
            self,
            slot_value: Any,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate user_nome_paciente"""
        comparar = tracker.get_slot("cenario_dois_menu")

        # Retornar cenario_dois_menu
        if slot_value == '#':
            return {"user_nome_paciente": None, "cenario_dois_menu": None}
        # Prosseguir para user_nome_paciente
        elif comparar == '4':
            if len(slot_value) <= 3 and not slot_value.isdigit():
                dispatcher.utter_message(text="Nome curto.")
                return {"user_nome_paciente": None}
            # validador
            else:
                return {"user_nome_paciente": slot_value}
        else:
            dispatcher.utter_message(response="utter_cenario_dois_resp_errada_voltar")
            return {"user_nome_paciente": None}

    def validate_user_nome_social(
            self,
            slot_value: Any,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate user_nome_social"""
        if slot_value == '#':
            return {"user_nome_paciente": None, "user_nome_social": None}
        else:
            return {"user_nome_social": slot_value}

    def validate_user_telefone(
            self,
            slot_value: Any,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate user_telefone"""

        if slot_value == '#':
            return {"user_nome_social": None}
        else:
            return {"user_telefone": slot_value}

    def validate_user_data_nasc(
            self,
            slot_value: Any,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate user_data_nasc"""

        if slot_value == '#':
            return {"user_telefone": None}
        else:
            return {"user_data_nasc": slot_value}

    def validate_user_sexo(
            self,
            slot_value: Any,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate user_sexo"""

        if slot_value == '#':
            return {"user_data_nasc": None}
        else:
            return {"user_sexo": slot_value}

    def validate_user_cpf(
            self,
            slot_value: Any,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate user_cpf"""

        if slot_value == '#':
            return {"user_sexo": None}
        else:
            return {"user_cpf": slot_value}

    def validate_user_nome_mae(
            self,
            slot_value: Any,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate user_nome_mae"""

        if slot_value == '#':
            return {"user_cpf": None}
        else:
            return {"user_nome_mae": slot_value}

    def validate_user_email(
            self,
            slot_value: Any,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate user_email"""

        if slot_value == '#':
            return {"user_nome_mae": None}
        else:
            return {"user_email": slot_value}

    def validate_user_end_cep(
            self,
            slot_value: Any,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate user_end_cep"""

        if slot_value == '#':
            return {"user_email": None}
        else:
            return {"user_end_cep": slot_value}

    def validate_user_end_rua(
            self,
            slot_value: Any,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate user_end_rua"""

        if slot_value == '#':
            return {"user_end_cep": None}
        else:
            return {"user_end_rua": slot_value}

    def validate_user_end_numero(
            self,
            slot_value: Any,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate user_end_numero"""

        if slot_value == '#':
            return {"user_end_rua": None}
        else:
            return {"user_end_numero": slot_value}

    def validate_user_end_complemento(
            self,
            slot_value: Any,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate user_end_complemento"""

        if slot_value == '#':
            return {"user_end_numero": None}
        else:
            return {"user_end_complemento": slot_value}

    def validate_user_end_bairro(
            self,
            slot_value: Any,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate user_end_bairro"""

        if slot_value == '#':
            return {"user_end_complemento": None}
        else:
            return {"user_end_bairro": slot_value}

    def validate_user_end_cidade(
            self,
            slot_value: Any,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate user_end_cidade"""

        if slot_value == '#':
            return {"user_end_bairro": None}
        else:
            return {"user_end_cidade": slot_value}

    def validate_user_numero_sus(
            self,
            slot_value: Any,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate user_numero_sus"""

        if slot_value == '#':
            return {"user_end_cidade": None}
        else:
            return {"user_numero_sus": slot_value}

    def validate_user_certidao_nascimento(
            self,
            slot_value: Any,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate user_certidao_nascimento"""

        if slot_value == '#':
            return {"user_numero_sus": None}
        else:
            return {"user_certidao_nascimento": slot_value}

    def validate_user_certidao_casamento(
            self,
            slot_value: Any,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate user_certidao_casamento"""

        if slot_value == '#':
            return {"user_certidao_nascimento": None}
        else:
            dispatcher.utter_message(response="utter_despedir")
            return {"user_certidao_casamento": slot_value}


