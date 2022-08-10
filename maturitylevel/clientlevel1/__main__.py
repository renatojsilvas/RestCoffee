from clientlevel1 import client
from clientlevel1.cli import build_parser

parser = build_parser()
args = parser.parse_args()

command = getattr(client, f'{args.command}_order')
params = vars(args)
del params['command']

print(command(**params))