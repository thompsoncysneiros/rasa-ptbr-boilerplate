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
            return {"requested_slot": None}
        elif data_cenario_dois_menu == '2':
            dispatcher.utter_message(response="utter_cenario_dois_menu_resp_dois")
            return {"requested_slot": None}
        elif data_cenario_dois_menu == '3':
            dispatcher.utter_message(response="utter_cenario_dois_menu_resp_tres")
            return {"requested_slot": None}
        elif data_cenario_dois_menu == '4':
            dispatcher.utter_message(response="utter_cenario_dois_menu_resp_quatro")
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

        return {"user_nome_paciente": slot_value}

    def validate_user_nome_social(
            self,
            slot_value: Any,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate user_nome_social"""

        return {"user_nome_social": slot_value}

    def validate_user_telefone(
            self,
            slot_value: Any,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate user_telefone"""

        return {"user_telefone": slot_value}

    def validate_user_data_nasc(
            self,
            slot_value: Any,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate user_data_nasc"""

        return {"user_data_nasc": slot_value}

    def validate_user_sexo(
            self,
            slot_value: Any,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate user_sexo"""

        return {"user_sexo": slot_value}

    def validate_user_cpf(
            self,
            slot_value: Any,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate user_cpf"""

        return {"user_cpf": slot_value}

    def validate_user_nome_mae(
            self,
            slot_value: Any,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate user_nome_mae"""

        return {"user_nome_mae": slot_value}

    def validate_user_email(
            self,
            slot_value: Any,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate user_email"""

        return {"user_email": slot_value}

    def validate_user_end_cep(
            self,
            slot_value: Any,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate user_end_cep"""

        return {"user_end_cep": slot_value}

    def validate_user_end_rua(
            self,
            slot_value: Any,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate user_end_rua"""

        return {"user_end_rua": slot_value}

    def validate_user_end_numero(
            self,
            slot_value: Any,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate user_end_numero"""

        return {"user_end_numero": slot_value}

    def validate_user_end_complemento(
            self,
            slot_value: Any,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate user_end_complemento"""

        return {"user_end_complemento": slot_value}

    def validate_user_end_bairro(
            self,
            slot_value: Any,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate user_end_bairro"""

        return {"user_end_bairro": slot_value}

    def validate_user_end_cidade(
            self,
            slot_value: Any,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate user_end_cidade"""

        return {"user_end_cidade": slot_value}

    def validate_user_numero_sus(
            self,
            slot_value: Any,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate user_numero_sus"""

        return {"user_numero_sus": slot_value}

    def validate_user_certidao_nascimento(
            self,
            slot_value: Any,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate user_certidao_nascimento"""

        return {"user_certidao_nascimento": slot_value}

    def validate_user_certidao_casamento(
            self,
            slot_value: Any,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate user_certidao_casamento"""

        dispatcher.utter_message(response="utter_despedir")
        return {"user_certidao_casamento": slot_value}


