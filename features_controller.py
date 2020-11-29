#####################################
########## Features #################
#####################################

# Standard Package
attachments_enabled = True
contact_card_enabled = False    # a bug needs to be fixed on mac first
# Premium Package
scheduled_sending = False
#
#
#
packages = ["normal", "standard", "premium"]
package = packages[0]   # CHOOSE WHICH PACKAGE TO COMPILE
# extras
multi_messages_enabled = True
repeat_every_24h = False
extra_var = None  # assign None to disable it. to activate it, put the column number





######################################
########### Functionilty #############
######################################

TYPE = "default"
version = "2.4.1"
language = "en"
demo = False

if TYPE == "default":
    # sheet settings
    header_row = False
    name_row = 1
    phone_row = 2
    country_code = None  # assign None to ignore it
    # Interface
    show_columns_note = True
    copyright_link = True
else:
    # sheet settings
    header_row = False
    name_row = 1
    phone_row = 2
    country_code = None    # assign None to ignore it
    # Interface
    show_columns_note = True
    copyright_link = True

################################################################
