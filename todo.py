# TODO: create booking history model --> booking_action, user_id, auto_time
# TODO: find model creation software using django
# TODO: create more tests
# TODO: add login required everywhere
# TODO: more or nicer seats layout
# TODO: add total number of seats, booked and unbooked to booking view

# logic for email regex
#  message = _('Enter a valid email address.')
#     code = 'invalid'
#     user_regex = _lazy_re_compile(
#         r"(^[-!#$%&'*+/=?^_`{}|~0-9A-Z]+(\.[-!#$%&'*+/=?^_`{}|~0-9A-Z]+)*\Z"  # dot-atom
#         r'|^"([\001-\010\013\014\016-\037!#-\[\]-\177]|\\[\001-\011\013\014\016-\177])*"\Z)',  # quoted-string
#         re.IGNORECASE)
#     domain_regex = _lazy_re_compile(
#         # max length for domain name labels is 63 characters per RFC 1034
#         r'((?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+)(?:[A-Z0-9-]{2,63}(?<!-))\Z',
#         re.IGNORECASE)
#     literal_regex = _lazy_re_compile(
#         # literal form, ipv4 or ipv6 address (SMTP 4.1.3)
#         r'\[([A-f0-9:\.]+)\]\Z',
#         re.IGNORECASE)
#     domain_whitelist = ['localhost']
