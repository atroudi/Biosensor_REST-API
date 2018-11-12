from app import db
from sqlalchemy.dialects.postgresql import JSON


class Records(db.Model):
    tablename__ = 'patientRecords'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String())
    api_secret = db.Column(db.String())

    sgv = db.Column(db.Integer)
    direction = db.Column(db.String())

    date = db.Column(db.Integer)
    dateString = db.Column(db.DateTime)

    rawData = db.Column(JSON)

    def __init__(self, username, api_secret, sgv, direction, data, dateTime, rawData):
        self.username = username
        self.api_secret = api_secret
        self.sgv = sgv
        self.direction = direction
        self.date = data
        self.dateString = dateTime
        self.rawData = rawData

    def __repr__(self):
        return '<id {}>'.format(self.id)


class AlembicVersion(db.Model):
    version_num = db.CharField(primary_key=True, max_length=32)

    class Meta:
        managed = False
        db_table = 'alembic_version'


class AuthGroup(db.Model):
    name = db.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(db.Model):
    group = db.ForeignKey(AuthGroup, db.DO_NOTHING)
    permission = db.ForeignKey('AuthPermission', db.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(db.Model):
    name = db.CharField(max_length=255)
    content_type = db.ForeignKey('DjangoContentType', db.DO_NOTHING)
    codename = db.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class DjangoAdminLog(db.Model):
    action_time = db.DateTimeField()
    object_id = db.TextField(blank=True, null=True)
    object_repr = db.CharField(max_length=200)
    action_flag = db.SmallIntegerField()
    change_message = db.TextField()
    content_type = db.ForeignKey('DjangoContentType', db.DO_NOTHING, blank=True, null=True)
    user = db.ForeignKey('UsersEmailuser', db.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(db.Model):
    app_label = db.CharField(max_length=100)
    model = db.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(db.Model):
    app = db.CharField(max_length=255)
    name = db.CharField(max_length=255)
    applied = db.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(db.Model):
    session_key = db.CharField(primary_key=True, max_length=40)
    session_data = db.TextField()
    expire_date = db.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class UsersEmailuser(db.Model):
    password = db.CharField(max_length=128)
    last_login = db.DateTimeField(blank=True, null=True)
    is_superuser = db.BooleanField()
    first_name = db.CharField(max_length=30)
    last_name = db.CharField(max_length=30)
    email = db.CharField(unique=True, max_length=254)
    is_staff = db.BooleanField()
    is_active = db.BooleanField()
    date_joined = db.DateTimeField()
    last_updated = db.DateTimeField()

    class Meta:
        managed = False
        db_table = 'users_emailuser'


class UsersEmailuserGroups(db.Model):
    emailuser = db.ForeignKey(UsersEmailuser, db.DO_NOTHING)
    group = db.ForeignKey(AuthGroup, db.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'users_emailuser_groups'
        unique_together = (('emailuser', 'group'),)


class UsersEmailuserUserPermissions(db.Model):
    emailuser = db.ForeignKey(UsersEmailuser, db.DO_NOTHING)
    permission = db.ForeignKey(AuthPermission, db.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'users_emailuser_user_permissions'
        unique_together = (('emailuser', 'permission'),)