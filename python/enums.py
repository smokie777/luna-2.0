VTS_EXPRESSIONS = {
  'FLUSHED': 'f7',
  'ANGRY': 'f9',
  'SAD': 'f4',
  'BROWN_HAIR': 'f11'
}

# maps to azure SSML speaking style tags
AZURE_SPEAKING_STYLE = {
  'WHISPERING': 'whispering'
}

TWITCH_EVENTS = {
  'BAN': 'BAN',
  'SUB': 'SUB',
  'BITS': 'BITS',
  'MESSAGE': 'MESSAGE'
}

PRIORITY_QUEUE_PRIORITY_MAP = {
  # highest priority
  'PRIORITY_BAN_USER': 1,
  'PRIORITY_GAME_INPUT': 2,
  'PRIORITY_IMAGE': 3,
  'PRIORITY_EVENTSUB_EVENTS_QUEUE': 4,
  'PRIORITY_MIC_INPUT': 5,
  'PRIORITY_COLLAB_MIC_INPUT': 6,
  'PRIORITY_REMIND_ME': 7,
  'PRIORITY_TWITCH_CHAT_QUEUE': 8,
  # lowest priority
}

PRIORITY_QUEUE_PRIORITIES = {
  # highest priority
  'PRIORITY_BAN_USER': 'PRIORITY_BAN_USER',
  'PRIORITY_GAME_INPUT': 'PRIORITY_GAME_INPUT',
  'PRIORITY_IMAGE': 'PRIORITY_IMAGE',
  'PRIORITY_EVENTSUB_EVENTS_QUEUE': 'PRIORITY_EVENTSUB_EVENTS_QUEUE',
  'PRIORITY_MIC_INPUT': 'PRIORITY_MIC_INPUT',
  'PRIORITY_COLLAB_MIC_INPUT': 'PRIORITY_COLLAB_MIC_INPUT',
  'PRIORITY_REMIND_ME': 'PRIORITY_REMIND_ME',
  'PRIORITY_TWITCH_CHAT_QUEUE': 'PRIORITY_TWITCH_CHAT_QUEUE',
  # lowest priority
}

TWITCH_EVENT_TYPE = {
  'CHANNEL_POINT_REDEMPTION': 'CHANNEL_POINT_REDEMPTION',
  'CHAT_COMMAND': 'CHAT_COMMAND'
}
