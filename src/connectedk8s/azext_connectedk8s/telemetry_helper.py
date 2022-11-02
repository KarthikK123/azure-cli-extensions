from opencensus.ext.azure.log_exporter import AzureLogHandler
from azure.cli.core import telemetry
from knack.log import get_logger

INSTRUMENTATION_KEY = "InstrumentationKey=0d592a02-bd1b-4d9e-8c99-e129fc4ffcd0;IngestionEndpoint=https://westus-0.in.applicationinsights.azure.com/;LiveEndpoint=https://westus.livediagnostics.monitor.azure.com/"
logger = get_logger(__name__)
logger.addHandler(AzureLogHandler(connection_string=INSTRUMENTATION_KEY))

def log_telemetry(message, current_command):
    logger.warning(message, extra={"custom_dimensions": {"command": current_command}})

def log_exception(exception, fault_type, summary):
    
    logger.error(exception, extra={"custom_dimensions": {"fault_type": fault_type, "summary": summary}})