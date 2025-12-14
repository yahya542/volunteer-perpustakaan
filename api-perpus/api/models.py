from django.db import models

class Biblio(models.Model):
    biblio_id = models.AutoField(primary_key=True)
    gmd_id = models.IntegerField(blank=True, null=True)
    title = models.TextField()
    sor = models.CharField(max_length=200, blank=True, null=True)
    edition = models.CharField(max_length=50, blank=True, null=True)
    isbn_issn = models.CharField(max_length=32, blank=True, null=True)
    publisher_id = models.IntegerField(blank=True, null=True)
    publish_year = models.CharField(max_length=20, blank=True, null=True)
    collation = models.CharField(max_length=50, blank=True, null=True)
    series_title = models.CharField(max_length=200, blank=True, null=True)
    call_number = models.CharField(max_length=50, blank=True, null=True)
    language_id = models.CharField(max_length=5, default='en')
    source = models.CharField(max_length=3, blank=True, null=True)
    publish_place_id = models.IntegerField(blank=True, null=True)
    classification = models.CharField(max_length=40, blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    image = models.CharField(max_length=100, blank=True, null=True)
    file_att = models.CharField(max_length=255, blank=True, null=True)
    opac_hide = models.SmallIntegerField(default=0)
    promoted = models.SmallIntegerField(default=0)
    labels = models.TextField(blank=True, null=True)
    frequency_id = models.IntegerField(default=0)
    spec_detail_info = models.TextField(blank=True, null=True)
    content_type_id = models.IntegerField(blank=True, null=True)
    media_type_id = models.IntegerField(blank=True, null=True)
    carrier_type_id = models.IntegerField(blank=True, null=True)
    input_date = models.DateTimeField(blank=True, null=True)
    last_update = models.DateTimeField(blank=True, null=True)
    uid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'biblio'
        indexes = [
            models.Index(fields=['gmd_id', 'publisher_id', 'language_id', 'publish_place_id']),
            models.Index(fields=['classification']),
            models.Index(fields=['opac_hide', 'promoted']),
            models.Index(fields=['content_type_id', 'media_type_id', 'carrier_type_id']),
            models.Index(fields=['uid']),
        ]

    def __str__(self):
        return self.title


class MstGmd(models.Model):
    gmd_id = models.AutoField(primary_key=True)
    gmd_code = models.CharField(max_length=3, blank=True, null=True, unique=True)
    gmd_name = models.CharField(max_length=30, unique=True)
    icon_image = models.CharField(max_length=100, blank=True, null=True)
    input_date = models.DateField()
    last_update = models.DateField(blank=True, null=True)

    class Meta:
        db_table = 'mst_gmd'

    def __str__(self):
        return self.gmd_name


class MstLanguage(models.Model):
    language_id = models.CharField(max_length=5, primary_key=True)
    language_name = models.CharField(max_length=20, unique=True)
    input_date = models.DateField(blank=True, null=True)
    last_update = models.DateField(blank=True, null=True)

    class Meta:
        db_table = 'mst_language'

    def __str__(self):
        return self.language_name


class MstPublisher(models.Model):
    publisher_id = models.AutoField(primary_key=True)
    publisher_name = models.CharField(max_length=100, unique=True)
    input_date = models.DateField()
    last_update = models.DateField(blank=True, null=True)

    class Meta:
        db_table = 'mst_publisher'

    def __str__(self):
        return self.publisher_name


class MstAuthor(models.Model):
    author_id = models.AutoField(primary_key=True)
    author_name = models.CharField(max_length=100, unique=True)
    author_year = models.CharField(max_length=20, blank=True, null=True)
    authority_type = models.CharField(max_length=1, default='p')
    auth_list = models.CharField(max_length=20, blank=True, null=True)
    input_date = models.DateField()
    last_update = models.DateField(blank=True, null=True)

    class Meta:
        db_table = 'mst_author'

    def __str__(self):
        return self.author_name


class BiblioAuthor(models.Model):
    biblio_id = models.IntegerField()
    author_id = models.IntegerField()
    level = models.IntegerField(default=1)

    class Meta:
        db_table = 'biblio_author'
        unique_together = ('biblio_id', 'author_id')

    def __str__(self):
        return f"Biblio {self.biblio_id} - Author {self.author_id}"


class LoanHistory(models.Model):
    loan_id = models.AutoField(primary_key=True)
    item_code = models.CharField(max_length=20)
    member_id = models.CharField(max_length=20)
    loan_date = models.DateField()
    due_date = models.DateField()
    return_date = models.DateField(blank=True, null=True)
    input_date = models.DateTimeField()
    last_update = models.DateTimeField(blank=True, null=True)
    uid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'loan_history'

    def __str__(self):
        return f"Loan {self.loan_id}"

class Item(models.Model):
    item_id = models.AutoField(primary_key=True)
    biblio_id = models.IntegerField(blank=True, null=True)
    call_number = models.CharField(max_length=50, blank=True, null=True)
    coll_type_id = models.IntegerField(blank=True, null=True)
    item_code = models.CharField(max_length=20, unique=True, blank=True, null=True)
    inventory_code = models.CharField(max_length=200, blank=True, null=True)
    received_date = models.DateField(blank=True, null=True)
    supplier_id = models.CharField(max_length=6, blank=True, null=True)
    order_no = models.CharField(max_length=20, blank=True, null=True)
    location_id = models.CharField(max_length=3, blank=True, null=True)
    order_date = models.DateField(blank=True, null=True)
    item_status_id = models.CharField(max_length=3, blank=True, null=True)
    site = models.CharField(max_length=50, blank=True, null=True)
    source = models.IntegerField(default=0)
    invoice = models.CharField(max_length=20, blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)
    price_currency = models.CharField(max_length=10, blank=True, null=True)
    invoice_date = models.DateField(blank=True, null=True)
    input_date = models.DateTimeField()
    last_update = models.DateTimeField(blank=True, null=True)
    uid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'item'
        indexes = [
            models.Index(fields=['uid']),
            models.Index(fields=['coll_type_id', 'location_id', 'item_status_id']),
            models.Index(fields=['biblio_id']),
        ]

    def __str__(self):
        return self.item_code or str(self.item_id)

class Loan(models.Model):
    loan_id = models.AutoField(primary_key=True)
    item_code = models.CharField(max_length=20, blank=True, null=True)
    member_id = models.CharField(max_length=20, blank=True, null=True)
    loan_date = models.DateField()
    due_date = models.DateField()
    renewed = models.IntegerField(default=0)
    loan_rules_id = models.IntegerField(default=0)
    actual = models.DateField(blank=True, null=True)
    is_lent = models.IntegerField(default=0)
    is_return = models.IntegerField(default=0)
    return_date = models.DateField(blank=True, null=True)
    input_date = models.DateTimeField(blank=True, null=True)
    last_update = models.DateTimeField(blank=True, null=True)
    uid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'loan'
        indexes = [
            models.Index(fields=['item_code']),
            models.Index(fields=['member_id']),
            models.Index(fields=['input_date', 'last_update', 'uid']),
        ]

    def __str__(self):
        return f"Loan {self.loan_id}"

class Reserve(models.Model):
    reserve_id = models.AutoField(primary_key=True)
    member_id = models.CharField(max_length=20)
    biblio_id = models.IntegerField()
    item_code = models.CharField(max_length=20)
    reserve_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'reserve'
        indexes = [
            models.Index(fields=['member_id', 'biblio_id']),
            models.Index(fields=['item_code']),
        ]

    def __str__(self):
        return f"Reserve {self.reserve_id}"

class Fines(models.Model):
    fines_id = models.AutoField(primary_key=True)
    fines_date = models.DateField()
    member_id = models.CharField(max_length=20)
    debet = models.IntegerField(default=0)
    credit = models.IntegerField(default=0)
    description = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fines'
        indexes = [
            models.Index(fields=['member_id']),
        ]

class MstLocation(models.Model):
    location_id = models.CharField(max_length=3, primary_key=True)
    location_name = models.CharField(max_length=100, blank=True, null=True, unique=True)
    input_date = models.DateField()
    last_update = models.DateField()

    class Meta:
        db_table = 'mst_location'

    def __str__(self):
        return self.location_name

class MstCollType(models.Model):
    coll_type_id = models.AutoField(primary_key=True)
    coll_type_name = models.CharField(max_length=30, unique=True)
    input_date = models.DateField(blank=True, null=True)
    last_update = models.DateField(blank=True, null=True)

    class Meta:
        db_table = 'mst_coll_type'

    def __str__(self):
        return self.coll_type_name

class MstItemStatus(models.Model):
    item_status_id = models.CharField(max_length=3, primary_key=True)
    item_status_name = models.CharField(max_length=30, unique=True)
    rules = models.CharField(max_length=255, blank=True, null=True)
    no_loan = models.SmallIntegerField(default=0)
    skip_stock_take = models.SmallIntegerField(default=0)
    input_date = models.DateField(blank=True, null=True)
    last_update = models.DateField(blank=True, null=True)

    class Meta:
        db_table = 'mst_item_status'

    def __str__(self):
        return self.item_status_name

class MstPlace(models.Model):
    place_id = models.AutoField(primary_key=True)
    place_name = models.CharField(max_length=30, unique=True)
    input_date = models.DateField(blank=True, null=True)
    last_update = models.DateField(blank=True, null=True)

    class Meta:
        db_table = 'mst_place'

    def __str__(self):
        return self.place_name

class MstSupplier(models.Model):
    supplier_id = models.AutoField(primary_key=True)
    supplier_name = models.CharField(max_length=100, unique=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    postal_code = models.CharField(max_length=10, blank=True, null=True)
    phone = models.CharField(max_length=14, blank=True, null=True)
    contact = models.CharField(max_length=30, blank=True, null=True)
    fax = models.CharField(max_length=14, blank=True, null=True)
    account = models.CharField(max_length=12, blank=True, null=True)
    e_mail = models.CharField(max_length=80, blank=True, null=True)
    input_date = models.DateField(blank=True, null=True)
    last_update = models.DateField(blank=True, null=True)

    class Meta:
        db_table = 'mst_supplier'

    def __str__(self):
        return self.supplier_name

class MstTopic(models.Model):
    topic_id = models.AutoField(primary_key=True)
    topic = models.CharField(max_length=50, unique=True)
    topic_type = models.CharField(max_length=2, choices=[
        ('t', 'Topic'),
        ('g', 'Geographic'),
        ('n', 'Name'),
        ('tm', 'Temporal'),
        ('gr', 'Genre'),
        ('oc', 'Occupation')
    ])
    auth_list = models.CharField(max_length=20, blank=True, null=True)
    classification = models.CharField(max_length=50)
    input_date = models.DateField(blank=True, null=True)
    last_update = models.DateField(blank=True, null=True)

    class Meta:
        db_table = 'mst_topic'

    def __str__(self):
        return self.topic

class MstFrequency(models.Model):
    frequency_id = models.AutoField(primary_key=True)
    frequency = models.CharField(max_length=25)
    language_prefix = models.CharField(max_length=5, blank=True, null=True)
    time_increment = models.SmallIntegerField(blank=True, null=True)
    time_unit = models.CharField(max_length=10, choices=[
        ('day', 'Day'),
        ('week', 'Week'),
        ('month', 'Month'),
        ('year', 'Year')
    ], default='day')
    input_date = models.DateField()
    last_update = models.DateField()

    class Meta:
        db_table = 'mst_frequency'

    def __str__(self):
        return self.frequency

class MstLoanRules(models.Model):
    loan_rules_id = models.AutoField(primary_key=True)
    member_type_id = models.IntegerField(default=0)
    coll_type_id = models.IntegerField(default=0)
    gmd_id = models.IntegerField(default=0)
    loan_limit = models.IntegerField(default=0)
    loan_periode = models.IntegerField(default=0)
    reborrow_limit = models.IntegerField(default=0)
    fine_each_day = models.IntegerField(default=0)
    grace_periode = models.SmallIntegerField(default=0)
    input_date = models.DateField(blank=True, null=True)
    last_update = models.DateField(blank=True, null=True)

    class Meta:
        db_table = 'mst_loan_rules'

    def __str__(self):
        return f"Loan Rules {self.loan_rules_id}"

class MstLabel(models.Model):
    label_id = models.AutoField(primary_key=True)
    label_name = models.CharField(max_length=20, unique=True)
    label_desc = models.CharField(max_length=50, blank=True, null=True)
    label_image = models.CharField(max_length=200)
    input_date = models.DateField()
    last_update = models.DateField()

    class Meta:
        db_table = 'mst_label'

    def __str__(self):
        return self.label_name

class MstCarrierType(models.Model):
    id = models.AutoField(primary_key=True)
    carrier_type = models.CharField(max_length=100, unique=True)
    code = models.CharField(max_length=5)
    code2 = models.CharField(max_length=1)
    input_date = models.DateTimeField()
    last_update = models.DateTimeField()

    class Meta:
        db_table = 'mst_carrier_type'
        indexes = [
            models.Index(fields=['code']),
        ]

    def __str__(self):
        return self.carrier_type

class MstContentType(models.Model):
    id = models.AutoField(primary_key=True)
    content_type = models.CharField(max_length=100, unique=True)
    code = models.CharField(max_length=5)
    code2 = models.CharField(max_length=1)
    input_date = models.DateTimeField()
    last_update = models.DateTimeField()

    class Meta:
        db_table = 'mst_content_type'
        indexes = [
            models.Index(fields=['code']),
        ]

    def __str__(self):
        return self.content_type

class MstMediaType(models.Model):
    id = models.AutoField(primary_key=True)
    media_type = models.CharField(max_length=100, unique=True)
    code = models.CharField(max_length=5)
    code2 = models.CharField(max_length=1)
    input_date = models.DateTimeField()
    last_update = models.DateTimeField()

    class Meta:
        db_table = 'mst_media_type'
        indexes = [
            models.Index(fields=['code']),
        ]

    def __str__(self):
        return self.media_type

class MstRelationTerm(models.Model):
    id = models.AutoField(primary_key=True)
    rt_id = models.CharField(max_length=11)
    rt_desc = models.CharField(max_length=50)

    class Meta:
        db_table = 'mst_relation_term'

    def __str__(self):
        return self.rt_desc

class MstVocCtrl(models.Model):
    vocabolary_id = models.AutoField(primary_key=True)
    topic_id = models.IntegerField()
    rt_id = models.CharField(max_length=11)
    related_topic_id = models.CharField(max_length=250)
    scope = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'mst_voc_ctrl'

    def __str__(self):
        return f"Voc Ctrl {self.vocabolary_id}"

class BiblioAttachment(models.Model):
    biblio_id = models.IntegerField()
    file_id = models.IntegerField()
    placement = models.CharField(max_length=20, choices=[
        ('link', 'Link'),
        ('popup', 'Popup'),
        ('embed', 'Embed')
    ], blank=True, null=True)
    access_type = models.CharField(max_length=10, choices=[
        ('public', 'Public'),
        ('private', 'Private')
    ])
    access_limit = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'biblio_attachment'
        indexes = [
            models.Index(fields=['biblio_id']),
            models.Index(fields=['file_id']),
            models.Index(fields=['biblio_id', 'file_id']),
        ]

    def __str__(self):
        return f"Attachment {self.biblio_id}-{self.file_id}"

class BiblioTopic(models.Model):
    biblio_id = models.IntegerField()
    topic_id = models.IntegerField()
    level = models.IntegerField(default=1)

    class Meta:
        db_table = 'biblio_topic'
        unique_together = ('biblio_id', 'topic_id')

    def __str__(self):
        return f"Biblio {self.biblio_id} - Topic {self.topic_id}"

class BiblioRelation(models.Model):
    biblio_id = models.IntegerField()
    rel_biblio_id = models.IntegerField()
    rel_type = models.IntegerField(default=1)

    class Meta:
        db_table = 'biblio_relation'
        unique_together = ('biblio_id', 'rel_biblio_id')

    def __str__(self):
        return f"Relation {self.biblio_id} - {self.rel_biblio_id}"

class BiblioCustom(models.Model):
    biblio_id = models.IntegerField(primary_key=True)

    class Meta:
        db_table = 'biblio_custom'

    def __str__(self):
        return str(self.biblio_id)

class SearchBiblio(models.Model):
    biblio_id = models.IntegerField(primary_key=True)
    title = models.TextField(blank=True, null=True)
    edition = models.CharField(max_length=50, blank=True, null=True)
    isbn_issn = models.CharField(max_length=20, blank=True, null=True)
    author = models.TextField(blank=True, null=True)
    topic = models.TextField(blank=True, null=True)
    gmd = models.CharField(max_length=30, blank=True, null=True)
    publisher = models.CharField(max_length=100, blank=True, null=True)
    publish_place = models.CharField(max_length=30, blank=True, null=True)
    language = models.CharField(max_length=20, blank=True, null=True)
    classification = models.CharField(max_length=40, blank=True, null=True)
    spec_detail_info = models.TextField(blank=True, null=True)
    carrier_type = models.CharField(max_length=100)
    content_type = models.CharField(max_length=100)
    media_type = models.CharField(max_length=100)
    location = models.TextField(blank=True, null=True)
    publish_year = models.CharField(max_length=20, blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    series_title = models.TextField(blank=True, null=True)
    items = models.TextField(blank=True, null=True)
    collection_types = models.TextField(blank=True, null=True)
    call_number = models.CharField(max_length=50, blank=True, null=True)
    opac_hide = models.SmallIntegerField(default=0)
    promoted = models.SmallIntegerField(default=0)
    labels = models.TextField(blank=True, null=True)
    collation = models.CharField(max_length=100, blank=True, null=True)
    image = models.CharField(max_length=100, blank=True, null=True)
    input_date = models.DateTimeField(blank=True, null=True)
    last_update = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'search_biblio'
        indexes = [
            models.Index(fields=['gmd', 'publisher', 'publish_place', 'language', 'classification', 'publish_year', 'call_number']),
            models.Index(fields=['opac_hide', 'promoted']),
            models.Index(fields=['carrier_type', 'media_type', 'content_type']),
        ]

    def __str__(self):
        return self.title or str(self.biblio_id)

class Kardex(models.Model):
    kardex_id = models.AutoField(primary_key=True)
    date_expected = models.DateField()
    date_received = models.DateField(blank=True, null=True)
    seq_number = models.CharField(max_length=25, blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    serial_id = models.IntegerField(blank=True, null=True)
    input_date = models.DateField()
    last_update = models.DateField()

    class Meta:
        db_table = 'kardex'
        indexes = [
            models.Index(fields=['serial_id']),
        ]

    def __str__(self):
        return f"Kardex {self.kardex_id}"

class Serial(models.Model):
    serial_id = models.AutoField(primary_key=True)
    date_start = models.DateField()
    date_end = models.DateField(blank=True, null=True)
    period = models.CharField(max_length=100, blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    biblio_id = models.IntegerField(blank=True, null=True)
    gmd_id = models.IntegerField(blank=True, null=True)
    input_date = models.DateField()
    last_update = models.DateField()

    class Meta:
        db_table = 'serial'
        indexes = [
            models.Index(fields=['biblio_id']),
            models.Index(fields=['gmd_id']),
        ]

    def __str__(self):
        return f"Serial {self.serial_id}"

class Holiday(models.Model):
    holiday_id = models.AutoField(primary_key=True)
    holiday_dayname = models.CharField(max_length=20)
    holiday_date = models.DateField(blank=True, null=True)
    description = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        db_table = 'holiday'
        unique_together = ('holiday_dayname', 'holiday_date')

    def __str__(self):
        return self.holiday_dayname

class StockTake(models.Model):
    stock_take_id = models.AutoField(primary_key=True)
    stock_take_name = models.CharField(max_length=200)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(blank=True, null=True)
    init_user = models.CharField(max_length=50)
    total_item_stock_taked = models.IntegerField(blank=True, null=True)
    total_item_lost = models.IntegerField(blank=True, null=True)
    total_item_exists = models.IntegerField(default=0)
    total_item_loan = models.IntegerField(blank=True, null=True)
    stock_take_users = models.TextField(blank=True, null=True)
    is_active = models.IntegerField(default=0)
    report_file = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'stock_take'

    def __str__(self):
        return self.stock_take_name

class StockTakeItem(models.Model):
    stock_take_id = models.IntegerField()
    item_id = models.IntegerField()
    item_code = models.CharField(max_length=20)
    title = models.CharField(max_length=255)
    gmd_name = models.CharField(max_length=30, blank=True, null=True)
    classification = models.CharField(max_length=30, blank=True, null=True)
    coll_type_name = models.CharField(max_length=30, blank=True, null=True)
    call_number = models.CharField(max_length=50, blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)
    status = models.CharField(max_length=10, choices=[
        ('e', 'Exists'),
        ('m', 'Missing'),
        ('u', 'Unknown'),
        ('l', 'Lost')
    ], default='m')
    checked_by = models.CharField(max_length=50)
    last_update = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'stock_take_item'
        unique_together = ('stock_take_id', 'item_id')
        indexes = [
            models.Index(fields=['item_code']),
            models.Index(fields=['status']),
            models.Index(fields=['gmd_name', 'classification', 'coll_type_name', 'location']),
        ]

    def __str__(self):
        return f"{self.item_code} - {self.title}"

class Files(models.Model):
    file_id = models.AutoField(primary_key=True)
    file_title = models.TextField()
    file_name = models.TextField()
    file_url = models.TextField(blank=True, null=True)
    file_dir = models.TextField(blank=True, null=True)
    mime_type = models.CharField(max_length=100, blank=True, null=True)
    file_desc = models.TextField(blank=True, null=True)
    file_key = models.TextField(blank=True, null=True)
    uploader_id = models.IntegerField()
    input_date = models.DateTimeField()
    last_update = models.DateTimeField()

    class Meta:
        db_table = 'files'
        indexes = [
            models.Index(fields=['file_name']),
            models.Index(fields=['file_dir']),
        ]

    def __str__(self):
        return self.file_title

class Content(models.Model):
    content_id = models.AutoField(primary_key=True)
    content_title = models.CharField(max_length=255)
    content_desc = models.TextField()
    content_path = models.CharField(max_length=20, unique=True)
    is_news = models.SmallIntegerField(blank=True, null=True)
    input_date = models.DateTimeField()
    last_update = models.DateTimeField()
    content_ownpage = models.CharField(max_length=1, choices=[('1', 'Yes'), ('2', 'No')], default='1')

    class Meta:
        db_table = 'content'

    def __str__(self):
        return self.content_title

class Setting(models.Model):
    setting_id = models.AutoField(primary_key=True)
    setting_name = models.CharField(max_length=30, unique=True)
    setting_value = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'setting'

    def __str__(self):
        return self.setting_name

class BackupLog(models.Model):
    backup_log_id = models.AutoField(primary_key=True)
    user_id = models.IntegerField(default=0)
    backup_time = models.DateTimeField()
    backup_file = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'backup_log'

    def __str__(self):
        return f"Backup {self.backup_log_id}"

class BiblioLog(models.Model):
    biblio_log_id = models.AutoField(primary_key=True)
    biblio_id = models.IntegerField()
    user_id = models.IntegerField()
    realname = models.CharField(max_length=100)
    title = models.TextField()
    ip = models.CharField(max_length=200)
    action = models.CharField(max_length=50)
    affectedrow = models.CharField(max_length=50)
    rawdata = models.TextField()
    additional_information = models.TextField()
    date = models.DateTimeField()

    class Meta:
        db_table = 'biblio_log'
        indexes = [
            models.Index(fields=['realname']),
            models.Index(fields=['biblio_id']),
            models.Index(fields=['user_id']),
            models.Index(fields=['ip']),
            models.Index(fields=['action']),
            models.Index(fields=['affectedrow']),
            models.Index(fields=['date']),
        ]

    def __str__(self):
        return f"Log {self.biblio_log_id}"

class FilesRead(models.Model):
    filelog_id = models.AutoField(primary_key=True)
    file_id = models.IntegerField()
    date_read = models.DateTimeField()
    member_id = models.CharField(max_length=20, blank=True, null=True)
    user_id = models.IntegerField(blank=True, null=True)
    client_ip = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        db_table = 'files_read'

    def __str__(self):
        return f"Read {self.filelog_id}"

class Plugins(models.Model):
    id = models.CharField(max_length=32, primary_key=True)
    path = models.TextField()
    created_at = models.DateTimeField()
    uid = models.IntegerField()

    class Meta:
        db_table = 'plugins'

    def __str__(self):
        return self.id

class IndexWords(models.Model):
    id = models.BigAutoField(primary_key=True)
    word = models.CharField(max_length=50)
    num_hits = models.IntegerField()
    doc_hits = models.IntegerField()

    class Meta:
        db_table = 'index_words'

    def __str__(self):
        return self.word

class IndexDocuments(models.Model):
    document_id = models.IntegerField()
    word_id = models.BigIntegerField()
    location = models.CharField(max_length=50)
    hit_count = models.IntegerField()

    class Meta:
        db_table = 'index_documents'
        unique_together = ('document_id', 'word_id', 'location')
        indexes = [
            models.Index(fields=['document_id']),
            models.Index(fields=['word_id']),
            models.Index(fields=['location']),
        ]

    def __str__(self):
        return f"Doc {self.document_id} - Word {self.word_id}"

class MstModule(models.Model):
    module_id = models.AutoField(primary_key=True)
    module_name = models.CharField(max_length=50, unique=True)
    module_path = models.CharField(max_length=200, blank=True, null=True)
    module_desc = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'mst_module'

    def __str__(self):
        return self.module_name

class MstServers(models.Model):
    server_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    uri = models.TextField()
    server_type = models.SmallIntegerField(default=1)  # 1 - p2p server; 2 - z3950; 3 - z3950 SRU
    input_date = models.DateTimeField()
    last_update = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'mst_servers'

    def __str__(self):
        return self.name

class MstCustomField(models.Model):
    field_id = models.AutoField(primary_key=True)
    primary_table = models.CharField(max_length=100, blank=True, null=True)
    dbfield = models.CharField(max_length=50, unique=True)
    label = models.CharField(max_length=80)
    type = models.CharField(max_length=20, choices=[
        ('text', 'Text'),
        ('checklist', 'Checklist'),
        ('numeric', 'Numeric'),
        ('dropdown', 'Dropdown'),
        ('longtext', 'Long Text'),
        ('choice', 'Choice'),
        ('date', 'Date')
    ])
    default = models.CharField(max_length=80, blank=True, null=True)
    max = models.IntegerField(blank=True, null=True)
    data = models.TextField(blank=True, null=True)
    indexed = models.SmallIntegerField(blank=True, null=True)
    class_field = models.CharField(max_length=100, blank=True, null=True)
    is_public = models.SmallIntegerField(blank=True, null=True)
    width = models.IntegerField(default=100)
    note = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'mst_custom_field'

    def __str__(self):
        return self.label

