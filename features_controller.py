#####################################
########## Features #################
#####################################

# Standard Package
contact_card_enabled = True
attachments_enabled = True
# Premium Package
scheduled_sending = False
#
# extra
multi_messages_enabled = False


######################################
########### Functionilty #############
######################################

TYPE = "default"
version = "2.3.1"
language = "en"
demo = True
# custom functionality
repeat_every_24h = False

if TYPE == "default":
    # sheet settings
    header_row = False
    name_row = 1
    phone_row = 2
    country_code = None  # assign None to ignore it
    extra_var = None  # assign None to ignore it
    # Interface
    show_columns_note = True
    copyright_link = True
else:
    # sheet settings
    header_row = False
    name_row = 1
    phone_row = 2
    country_code = None    # assign None to ignore it
    extra_var = 3    # assign None to ignore it
    # Interface
    show_columns_note = True
    copyright_link = True

################################################################
