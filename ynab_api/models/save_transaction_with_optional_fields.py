# coding: utf-8

"""
    YNAB API Endpoints

    Our API uses a REST based design, leverages the JSON data format, and relies upon HTTPS for transport. We respond with meaningful HTTP response codes and if an error occurs, we include error details in the response body.  API Documentation is at https://api.ynab.com  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class SaveTransactionWithOptionalFields(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'account_id': 'str',
        '_date': 'date',
        'amount': 'int',
        'payee_id': 'str',
        'payee_name': 'str',
        'category_id': 'str',
        'memo': 'str',
        'cleared': 'str',
        'approved': 'bool',
        'flag_color': 'str',
        'import_id': 'str',
        'subtransactions': 'list[SaveSubTransaction]'
    }

    attribute_map = {
        'account_id': 'account_id',
        '_date': 'date',
        'amount': 'amount',
        'payee_id': 'payee_id',
        'payee_name': 'payee_name',
        'category_id': 'category_id',
        'memo': 'memo',
        'cleared': 'cleared',
        'approved': 'approved',
        'flag_color': 'flag_color',
        'import_id': 'import_id',
        'subtransactions': 'subtransactions'
    }

    def __init__(self, account_id=None, _date=None, amount=None, payee_id=None, payee_name=None, category_id=None, memo=None, cleared=None, approved=None, flag_color=None, import_id=None, subtransactions=None):  # noqa: E501
        """SaveTransactionWithOptionalFields - a model defined in Swagger"""  # noqa: E501
        self._account_id = None
        self.__date = None
        self._amount = None
        self._payee_id = None
        self._payee_name = None
        self._category_id = None
        self._memo = None
        self._cleared = None
        self._approved = None
        self._flag_color = None
        self._import_id = None
        self._subtransactions = None
        self.discriminator = None
        if account_id is not None:
            self.account_id = account_id
        if _date is not None:
            self._date = _date
        if amount is not None:
            self.amount = amount
        if payee_id is not None:
            self.payee_id = payee_id
        if payee_name is not None:
            self.payee_name = payee_name
        if category_id is not None:
            self.category_id = category_id
        if memo is not None:
            self.memo = memo
        if cleared is not None:
            self.cleared = cleared
        if approved is not None:
            self.approved = approved
        if flag_color is not None:
            self.flag_color = flag_color
        if import_id is not None:
            self.import_id = import_id
        if subtransactions is not None:
            self.subtransactions = subtransactions

    @property
    def account_id(self):
        """Gets the account_id of this SaveTransactionWithOptionalFields.  # noqa: E501


        :return: The account_id of this SaveTransactionWithOptionalFields.  # noqa: E501
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this SaveTransactionWithOptionalFields.


        :param account_id: The account_id of this SaveTransactionWithOptionalFields.  # noqa: E501
        :type: str
        """

        self._account_id = account_id

    @property
    def _date(self):
        """Gets the _date of this SaveTransactionWithOptionalFields.  # noqa: E501

        The transaction date in ISO format (e.g. 2016-12-01).  Future dates (scheduled transactions) are not permitted.  Split transaction dates cannot be changed and if a different date is supplied it will be ignored.  # noqa: E501

        :return: The _date of this SaveTransactionWithOptionalFields.  # noqa: E501
        :rtype: date
        """
        return self.__date

    @_date.setter
    def _date(self, _date):
        """Sets the _date of this SaveTransactionWithOptionalFields.

        The transaction date in ISO format (e.g. 2016-12-01).  Future dates (scheduled transactions) are not permitted.  Split transaction dates cannot be changed and if a different date is supplied it will be ignored.  # noqa: E501

        :param _date: The _date of this SaveTransactionWithOptionalFields.  # noqa: E501
        :type: date
        """

        self.__date = _date

    @property
    def amount(self):
        """Gets the amount of this SaveTransactionWithOptionalFields.  # noqa: E501

        The transaction amount in milliunits format.  Split transaction amounts cannot be changed and if a different amount is supplied it will be ignored.  # noqa: E501

        :return: The amount of this SaveTransactionWithOptionalFields.  # noqa: E501
        :rtype: int
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this SaveTransactionWithOptionalFields.

        The transaction amount in milliunits format.  Split transaction amounts cannot be changed and if a different amount is supplied it will be ignored.  # noqa: E501

        :param amount: The amount of this SaveTransactionWithOptionalFields.  # noqa: E501
        :type: int
        """

        self._amount = amount

    @property
    def payee_id(self):
        """Gets the payee_id of this SaveTransactionWithOptionalFields.  # noqa: E501

        The payee for the transaction.  To create a transfer between two accounts, use the account transfer payee pointing to the target account.  Account transfer payees are specified as `tranfer_payee_id` on the account resource.  # noqa: E501

        :return: The payee_id of this SaveTransactionWithOptionalFields.  # noqa: E501
        :rtype: str
        """
        return self._payee_id

    @payee_id.setter
    def payee_id(self, payee_id):
        """Sets the payee_id of this SaveTransactionWithOptionalFields.

        The payee for the transaction.  To create a transfer between two accounts, use the account transfer payee pointing to the target account.  Account transfer payees are specified as `tranfer_payee_id` on the account resource.  # noqa: E501

        :param payee_id: The payee_id of this SaveTransactionWithOptionalFields.  # noqa: E501
        :type: str
        """

        self._payee_id = payee_id

    @property
    def payee_name(self):
        """Gets the payee_name of this SaveTransactionWithOptionalFields.  # noqa: E501

        The payee name.  If a `payee_name` value is provided and `payee_id` has a null value, the `payee_name` value will be used to resolve the payee by either (1) a matching payee rename rule (only if `import_id` is also specified) or (2) a payee with the same name or (3) creation of a new payee.  # noqa: E501

        :return: The payee_name of this SaveTransactionWithOptionalFields.  # noqa: E501
        :rtype: str
        """
        return self._payee_name

    @payee_name.setter
    def payee_name(self, payee_name):
        """Sets the payee_name of this SaveTransactionWithOptionalFields.

        The payee name.  If a `payee_name` value is provided and `payee_id` has a null value, the `payee_name` value will be used to resolve the payee by either (1) a matching payee rename rule (only if `import_id` is also specified) or (2) a payee with the same name or (3) creation of a new payee.  # noqa: E501

        :param payee_name: The payee_name of this SaveTransactionWithOptionalFields.  # noqa: E501
        :type: str
        """

        self._payee_name = payee_name

    @property
    def category_id(self):
        """Gets the category_id of this SaveTransactionWithOptionalFields.  # noqa: E501

        The category for the transaction.  To configure a split transaction, you can specify null for `category_id` and provide a `subtransactions` array as part of the transaction object.  If an existing transaction is a split, the `category_id` cannot be changed.  Credit Card Payment categories are not permitted and will be ignored if supplied.  # noqa: E501

        :return: The category_id of this SaveTransactionWithOptionalFields.  # noqa: E501
        :rtype: str
        """
        return self._category_id

    @category_id.setter
    def category_id(self, category_id):
        """Sets the category_id of this SaveTransactionWithOptionalFields.

        The category for the transaction.  To configure a split transaction, you can specify null for `category_id` and provide a `subtransactions` array as part of the transaction object.  If an existing transaction is a split, the `category_id` cannot be changed.  Credit Card Payment categories are not permitted and will be ignored if supplied.  # noqa: E501

        :param category_id: The category_id of this SaveTransactionWithOptionalFields.  # noqa: E501
        :type: str
        """

        self._category_id = category_id

    @property
    def memo(self):
        """Gets the memo of this SaveTransactionWithOptionalFields.  # noqa: E501


        :return: The memo of this SaveTransactionWithOptionalFields.  # noqa: E501
        :rtype: str
        """
        return self._memo

    @memo.setter
    def memo(self, memo):
        """Sets the memo of this SaveTransactionWithOptionalFields.


        :param memo: The memo of this SaveTransactionWithOptionalFields.  # noqa: E501
        :type: str
        """

        self._memo = memo

    @property
    def cleared(self):
        """Gets the cleared of this SaveTransactionWithOptionalFields.  # noqa: E501

        The cleared status of the transaction  # noqa: E501

        :return: The cleared of this SaveTransactionWithOptionalFields.  # noqa: E501
        :rtype: str
        """
        return self._cleared

    @cleared.setter
    def cleared(self, cleared):
        """Sets the cleared of this SaveTransactionWithOptionalFields.

        The cleared status of the transaction  # noqa: E501

        :param cleared: The cleared of this SaveTransactionWithOptionalFields.  # noqa: E501
        :type: str
        """
        allowed_values = ["cleared", "uncleared", "reconciled"]  # noqa: E501
        if cleared not in allowed_values:
            raise ValueError(
                "Invalid value for `cleared` ({0}), must be one of {1}"  # noqa: E501
                .format(cleared, allowed_values)
            )

        self._cleared = cleared

    @property
    def approved(self):
        """Gets the approved of this SaveTransactionWithOptionalFields.  # noqa: E501

        Whether or not the transaction is approved.  If not supplied, transaction will be unapproved by default.  # noqa: E501

        :return: The approved of this SaveTransactionWithOptionalFields.  # noqa: E501
        :rtype: bool
        """
        return self._approved

    @approved.setter
    def approved(self, approved):
        """Sets the approved of this SaveTransactionWithOptionalFields.

        Whether or not the transaction is approved.  If not supplied, transaction will be unapproved by default.  # noqa: E501

        :param approved: The approved of this SaveTransactionWithOptionalFields.  # noqa: E501
        :type: bool
        """

        self._approved = approved

    @property
    def flag_color(self):
        """Gets the flag_color of this SaveTransactionWithOptionalFields.  # noqa: E501

        The transaction flag  # noqa: E501

        :return: The flag_color of this SaveTransactionWithOptionalFields.  # noqa: E501
        :rtype: str
        """
        return self._flag_color

    @flag_color.setter
    def flag_color(self, flag_color):
        """Sets the flag_color of this SaveTransactionWithOptionalFields.

        The transaction flag  # noqa: E501

        :param flag_color: The flag_color of this SaveTransactionWithOptionalFields.  # noqa: E501
        :type: str
        """
        allowed_values = ["red", "orange", "yellow", "green", "blue", "purple"]  # noqa: E501
        if flag_color not in allowed_values:
            raise ValueError(
                "Invalid value for `flag_color` ({0}), must be one of {1}"  # noqa: E501
                .format(flag_color, allowed_values)
            )

        self._flag_color = flag_color

    @property
    def import_id(self):
        """Gets the import_id of this SaveTransactionWithOptionalFields.  # noqa: E501

        If specified, the new transaction will be assigned this `import_id` and considered \"imported\".  We will also attempt to match this imported transaction to an existing \"user-entered\" transation on the same account, with the same amount, and with a date +/-10 days from the imported transaction date.<br><br>Transactions imported through File Based Import or Direct Import (not through the API) are assigned an import_id in the format: 'YNAB:[milliunit_amount]:[iso_date]:[occurrence]'. For example, a transaction dated 2015-12-30 in the amount of -$294.23 USD would have an import_id of 'YNAB:-294230:2015-12-30:1'.  If a second transaction on the same account was imported and had the same date and same amount, its import_id would be 'YNAB:-294230:2015-12-30:2'.  Using a consistent format will prevent duplicates through Direct Import and File Based Import.<br><br>If import_id is omitted or specified as null, the transaction will be treated as a \"user-entered\" transaction. As such, it will be eligible to be matched against transactions later being imported (via DI, FBI, or API).  # noqa: E501

        :return: The import_id of this SaveTransactionWithOptionalFields.  # noqa: E501
        :rtype: str
        """
        return self._import_id

    @import_id.setter
    def import_id(self, import_id):
        """Sets the import_id of this SaveTransactionWithOptionalFields.

        If specified, the new transaction will be assigned this `import_id` and considered \"imported\".  We will also attempt to match this imported transaction to an existing \"user-entered\" transation on the same account, with the same amount, and with a date +/-10 days from the imported transaction date.<br><br>Transactions imported through File Based Import or Direct Import (not through the API) are assigned an import_id in the format: 'YNAB:[milliunit_amount]:[iso_date]:[occurrence]'. For example, a transaction dated 2015-12-30 in the amount of -$294.23 USD would have an import_id of 'YNAB:-294230:2015-12-30:1'.  If a second transaction on the same account was imported and had the same date and same amount, its import_id would be 'YNAB:-294230:2015-12-30:2'.  Using a consistent format will prevent duplicates through Direct Import and File Based Import.<br><br>If import_id is omitted or specified as null, the transaction will be treated as a \"user-entered\" transaction. As such, it will be eligible to be matched against transactions later being imported (via DI, FBI, or API).  # noqa: E501

        :param import_id: The import_id of this SaveTransactionWithOptionalFields.  # noqa: E501
        :type: str
        """

        self._import_id = import_id

    @property
    def subtransactions(self):
        """Gets the subtransactions of this SaveTransactionWithOptionalFields.  # noqa: E501

        An array of subtransactions to configure a transaction as a split.  Updating `subtransactions` on an existing split transaction is not supported.  # noqa: E501

        :return: The subtransactions of this SaveTransactionWithOptionalFields.  # noqa: E501
        :rtype: list[SaveSubTransaction]
        """
        return self._subtransactions

    @subtransactions.setter
    def subtransactions(self, subtransactions):
        """Sets the subtransactions of this SaveTransactionWithOptionalFields.

        An array of subtransactions to configure a transaction as a split.  Updating `subtransactions` on an existing split transaction is not supported.  # noqa: E501

        :param subtransactions: The subtransactions of this SaveTransactionWithOptionalFields.  # noqa: E501
        :type: list[SaveSubTransaction]
        """

        self._subtransactions = subtransactions

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(SaveTransactionWithOptionalFields, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, SaveTransactionWithOptionalFields):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
