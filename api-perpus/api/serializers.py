from rest_framework import serializers
from .models import (
    Biblio, Item, Loan, Reserve, Fines, LoanHistory,
    MstGmd, MstLanguage, MstLocation, MstCollType, MstItemStatus,
    MstPublisher, MstPlace, MstSupplier, MstAuthor, MstTopic,
    MstFrequency, MstLoanRules, MstLabel, Setting
)

class BiblioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Biblio
        fields = '__all__'
        read_only_fields = ['biblio_id', 'input_date', 'last_update']

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'
        read_only_fields = ['item_id', 'input_date', 'last_update']

class LoanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Loan
        fields = '__all__'
        read_only_fields = ['loan_id', 'input_date', 'last_update']

class ReserveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reserve
        fields = '__all__'
        read_only_fields = ['reserve_id']

class FinesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fines
        fields = '__all__'
        read_only_fields = ['fines_id']

class MstGmdSerializer(serializers.ModelSerializer):
    class Meta:
        model = MstGmd
        fields = '__all__'
        read_only_fields = ['gmd_id', 'input_date', 'last_update']

class MstLanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = MstLanguage
        fields = '__all__'
        read_only_fields = ['input_date', 'last_update']

class MstLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = MstLocation
        fields = '__all__'
        read_only_fields = ['input_date', 'last_update']

class MstCollTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = MstCollType
        fields = '__all__'
        read_only_fields = ['coll_type_id', 'input_date', 'last_update']

class MstItemStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = MstItemStatus
        fields = '__all__'
        read_only_fields = ['input_date', 'last_update']

class MstPublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = MstPublisher
        fields = '__all__'
        read_only_fields = ['publisher_id', 'input_date', 'last_update']

class MstPlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = MstPlace
        fields = '__all__'
        read_only_fields = ['place_id', 'input_date', 'last_update']

class MstSupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = MstSupplier
        fields = '__all__'
        read_only_fields = ['supplier_id', 'input_date', 'last_update']

class MstAuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = MstAuthor
        fields = '__all__'
        read_only_fields = ['author_id', 'input_date', 'last_update']

class MstTopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = MstTopic
        fields = '__all__'
        read_only_fields = ['topic_id', 'input_date', 'last_update']

class MstFrequencySerializer(serializers.ModelSerializer):
    class Meta:
        model = MstFrequency
        fields = '__all__'
        read_only_fields = ['frequency_id', 'input_date', 'last_update']

class MstLoanRulesSerializer(serializers.ModelSerializer):
    class Meta:
        model = MstLoanRules
        fields = '__all__'
        read_only_fields = ['loan_rules_id', 'input_date', 'last_update']

class MstLabelSerializer(serializers.ModelSerializer):
    class Meta:
        model = MstLabel
        fields = '__all__'
        read_only_fields = ['label_id', 'input_date', 'last_update']

class LoanHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = LoanHistory
        fields = '__all__'
        read_only_fields = ['loan_id']

class SettingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Setting
        fields = '__all__'
        read_only_fields = ['setting_id']