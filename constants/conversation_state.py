from telegram.ext import ConversationHandler

# State definitions for top level conversation
SELECTING_ACTION = "SELECTING_ACTION"
ADDING_MEMBER = "ADDING_MEMBER"
ADDING_SELF = "ADDING_SELF"
DESCRIBING_SELF = "DESCRIBING_SELF"

# State definitions for second level conversation
SELECTING_LEVEL, SELECTING_GENDER = "SELECTING_LEVEL", "SELECTING_GENDER"

# State definitions for descriptions conversation
SELECTING_FEATURE, TYPING = "SELECTING_FEATURE", "TYPING"

# Meta states
STOPPING, SHOWING = "STOPPING", "SHOWING"

# Shortcut for ConversationHandler.END
END = ConversationHandler.END
