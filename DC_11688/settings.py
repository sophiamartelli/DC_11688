

BOT_NAME = 'DC_11688'

SPIDER_MODULES = ['DC_11688.spiders']
NEWSPIDER_MODULE = 'DC_11688.spiders'


ROBOTSTXT_OBEY = False







SEEDS = {
    'Biocides': 'https://consultations.hse.gov.uk/consultation_finder/?sort_on=iconsultable_modifieddate&sort_order=descending&advanced=1&tx=&st=&au=&in=Biocides&de=',
    'CLP': 'https://consultations.hse.gov.uk/consultation_finder/?sort_on=iconsultable_modifieddate&sort_order=descending&advanced=1&tx=&st=&au=&in=CLP&de=',
    'Ecotoxicology': 'https://consultations.hse.gov.uk/consultation_finder/?sort_on=iconsultable_modifieddate&sort_order=descending&advanced=1&tx=&st=&au=&in=Ecotoxicology&de=',
    'REACH': 'https://consultations.hse.gov.uk/consultation_finder/?sort_on=iconsultable_modifieddate&sort_order=descending&advanced=1&tx=&st=&au=&in=Registration%2C+Evaluation%2C+Authorisation+%26+restriction+of+CHemicals+%28REACH%29&de=',
}
