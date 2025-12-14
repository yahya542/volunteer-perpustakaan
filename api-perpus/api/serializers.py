from rest_framework import serializers
from .models import (
    Biblio, LoanHistory
)

class BiblioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Biblio
        fields = '__all__'
        read_only_fields = ['biblio_id', 'input_date', 'last_update']

class LoanHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = LoanHistory
        fields = '__all__'
        read_only_fields = ['loan_id']

class DetailedBiblioSerializer(serializers.ModelSerializer):
    authors = serializers.SerializerMethodField()
    publisher = serializers.SerializerMethodField()
    language = serializers.SerializerMethodField()
    gmd = serializers.SerializerMethodField()
    
    class Meta:
        model = Biblio
        fields = '__all__'
        read_only_fields = ['biblio_id', 'input_date', 'last_update']
    
    def get_authors(self, obj):
        # Import here to avoid circular imports
        from .models import BiblioAuthor, MstAuthor
        # Get all authors related to this biblio entry
        try:
            biblio_authors = BiblioAuthor.objects.filter(biblio_id=obj.biblio_id)
            author_data = []
            for ba in biblio_authors:
                try:
                    author = MstAuthor.objects.get(author_id=ba.author_id)
                    author_data.append({
                        'author_id': author.author_id,
                        'author_name': author.author_name,
                        'author_year': author.author_year,
                        'authority_type': author.authority_type
                    })
                except MstAuthor.DoesNotExist:
                    continue
            return author_data
        except Exception as e:
            # Return empty list if there's any error
            return []
    
    def get_publisher(self, obj):
        # Import here to avoid circular imports
        from .models import MstPublisher
        # Get publisher information
        if obj.publisher_id:
            try:
                publisher = MstPublisher.objects.get(publisher_id=obj.publisher_id)
                return {
                    'publisher_id': publisher.publisher_id,
                    'publisher_name': publisher.publisher_name
                }
            except MstPublisher.DoesNotExist:
                return None
        return None
    
    def get_language(self, obj):
        # Import here to avoid circular imports
        from .models import MstLanguage
        # Get language information
        if obj.language_id:
            try:
                language = MstLanguage.objects.get(language_id=obj.language_id)
                return {
                    'language_id': language.language_id,
                    'language_name': language.language_name
                }
            except MstLanguage.DoesNotExist:
                return None
        return None
    
    def get_gmd(self, obj):
        # Import here to avoid circular imports
        from .models import MstGmd
        # Get GMD (General Material Designation) information
        if obj.gmd_id:
            try:
                gmd = MstGmd.objects.get(gmd_id=obj.gmd_id)
                return {
                    'gmd_id': gmd.gmd_id,
                    'gmd_code': gmd.gmd_code,
                    'gmd_name': gmd.gmd_name
                }
            except MstGmd.DoesNotExist:
                return None
        return None