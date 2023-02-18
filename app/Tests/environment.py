import behave
from ipdb import sset_trace, post_mortem
from pytest import fixture, use_fixture
from pyspark.sql import SparkSession

def before_all(context):
    context.config.setup_logging()
    global BEHAVE_DEBUG_ON_ERROR
    BEHAVE_DEBUG_ON_ERROR = True

@fixture
def spark_session(context):
    context.spark = SparkSession.builder.getOrCreate()

def before_tag(context, tag):
    if tag == 'fixture.spark.session':
        use_fixture(spark_session, context)

def before_feature(context, feature):
    print('Analyzing feature: {feature}')

def before_scenario(context, scenario):
    print('Analyzing scenario: {scenario}')

def after_step(context, step):
    if BEHAVE_DEBUG_ON_ERROR and step.status == 'failed':
        sset_trace()
        post_mortem(step.exc_traceback)

def after_scenario(context, scenario):
    print('Ending scenario: {scenario}')

def after_all(context):
    ...