import random


"""
Returns a "random"  10 word adjective list.

"""


adjectives = [
    'abject',
    'able',
    'abnormal',
    'abrupt',
    'absent',
    'absentminded',
    'absolute',
    'absorbing',
    'abstemious',
    'abstract',
    'abstruse',
    'absurd',
    'abundant',
    'abusive',
    'abysmal',
    'academic',
    'acapella',
    'acceptant',
    'accidental',
    'according',
    'accurate',
    'accusing',
    'acquiescent',
    'acquisitive',
    'acrostic',
    'active',
    'actual',
    'acute',
    'adamant',
    'addictive',
    'additional',
    'adept',
    'adequate',
    'adjectival',
    'admirable',
    'admiring',
    'admissible',
    'admitted',
    'adoptive',
    'adorable',
    'adroit',
    'adventitious',
    'adverbial',
    'adversarial',
    'adverse',
    'aerodynamic',
    'aesthetic',
    'affable',
    'affected',
    'affecting',
    'affectionate',
    'affirmative',
    'afflictive',
    'afresh',
    'again',
    'aggravated',
    'aggressive',
    'agonizing',
    'agreeable',
    'aimless',
    'alarmed',
    'alert',
    'alleged',
    'allusive',
    'aloud',
    'alphabetical',
    'alternate',
    'altruistic',
    'always',
    'amateur',
    'amazed',
    'amazing',
    'ambidextrous',
    'ambiguous',
    'ambitious',
    'amiable',
    'amicable',
    'amoral',
    'amorous',
    'amp',
    'amused',
    'analogical',
    'ancient',
    'anew',
    'angelic',
    'angry',
    'annoyed',
    'annoying',
    'annual',
    'anonymous',
    'antagonistic',
    'antiseptic',
    'anxious',
    'anyhow',
    'anymore',
    'anyplace',
    'anyway',
    'anywhere',
    'anywise',
    'apathetic',
    'apocryphal',
    'apologetic',
    'appalling',
    'apparent',
    'appealing',
    'appeasing',
    'appetizing',
    'apposite',
    'appreciable',
    'appreciative',
    'apprehensive',
    'appropriate',
    'approving',
    'approximate',
    'arbitrary',
    'archaic',
    'archaic',
    'ardent',
    'arduous',
    'aroused',
    'arrogant',
    'artful',
    'articulate',
    'artificial',
    'artic',
    'artistic',
    'artistic',
    'artless',
    'aswell',
    'ashamed',
    'assiduous',
    'assuring',
    'astonished',
    'astonishing',
    'astounding',
    'astute',
    'athletic',
    'atilt',
    'atonal',
    'atrocious',
    'attentive',
    'attractive',
    'audacious',
    'audible',
    'auspicious',
    'austere',
    'authentic',
    'authoritative',
    'autocratic',
    'automatic',
    'autonomic',
    'autonomous',
    'avid',
    'awful',
    'awkward',
    'awry',
    'backwards',
    'bad',
    'baffling',
    'baggy',
    'baleful',
    'barbarous',
    'barebacked',
    'barefooted',
    'barehanded',
    'bareheaded',
    'bashful',
    'basic',
    'bawdy',
    'beauteous',
    'beautiful',
    'becoming',
    'beforehand',
    'begging',
    'behindhand',
    'belated',
    'believable',
    'believing',
    'belligerent',
    'bemused',
    'beneficial',
    'benevolent',
    'benign',
    'bestial',
    'betwixted',
    'biannual',
    'biennial',
    'bigheaded',
    'bilateral',
    'bitter',
    'bizarre',
    'bizarre',
    'blaming',
    'bland',
    'blank',
    'blasphemous',
    'blatant',
    'bleak',
    'blessing',
    'blind',
    'blissful',
    'blithe',
    'bloodthirsty',
    'blunt',
    'blushing',
    'boastful',
    'boisterous',
    'bold',
    'bootless',
    'bored',
    'bounteous',
    'bountiful',
    'boyish',
    'brash',
    'brave',
    'brazen',
    'breathless',
    'brief',
    'bright',
    'brilliant',
    'brisk',
    'broad',
    'broken',
    'brother',
    'brusque',
    'brutal',
    'busy',
    'buzzing',
    'cadaverous',
    'caddish',
    'cagey',
    'calamitous',
    'calculable',
    'callous',
    'calm',
    'calumnious',
    'candid',
    'canny',
    'canonical',
    'cantabile',
    'cantankerous',
    'capable',
    'capacious',
    'capitalistic',
    'capital',
    'capricious',
    'captious',
    'cardinal',
    'careful',
    'careless',
    'caring',
    'carnal',
    'carnivorous',
    'casual',
    'categorical',
    'catty',
    'caudal',
    'causal',
    'causeless',
    'caustic',
    'cautious',
    'cavalier',
    'cavernous',
    'ceaseless',
    'celestial',
    'censorious',
    'centennial',
    'central',
    'centrifugal',
    'centripetal',
    'ceremonial',
    'ceremonious',
    'certain',
    'challenging',
    'chaotic',
    'characteristic',
    'chary',
    'charitable',
    'charming',
    'chaste',
    'chatty',
    'chauvinistic',
    'cheap',
    'cheeky',
    'cheerful',
    'cheery',
    'cheerless',
    'chief',
    'childish',
    'chilling',
    'chivalrous',
    'choppy',
    'choral',
    'chronic',
    'chronological',
    'chummy',
    'churlish',
    'circumstantial',
    'civic',
    'civil',
    'classical',
    'clean',
    'clear',
    'clever',
    'clinical',
    'clockwise',
    'close',
    'clownish',
    'clueless',
    'clumsy',
    'coarse',
    'coeducational',
    'coequal',
    'cogent',
    'coherent',
    'cold',
    'collective',
    'colossal',
    'coltish',
    'comfortable',
    'comforting',
    'comical',
    'commanding',
    'commercial',
    'common',
    'compact',
    'comparative',
    'compassionate',
    'compelling',
    'competent',
    'competitive',
    'complacent',
    'complete',
    'complicated',
    'composed',
    'comprehensive',
    'compulsive',
    'conceited',
    'conceivable',
    'concerned',
    'conclusive',
    'condescending',
    'conditional',
    'confessed',
    'confessing',
    'confidential',
    'confident',
    'confirming',
    'confused',
    'confusing',
    'conscientious',
    'conscious',
    'consecutive',
    'consequent',
    'conservative',
    'considerable',
    'considerate',
    'consistent',
    'conspicuous',
    'conspiratorial',
    'conspiring',
    'constant',
    'constructive',
    'consumed',
    'contemptible',
    'contemptuous',
    'contented',
    'content',
    'conterminous',
    'continual',
    'continuous',
    'contractual',
    'contradictive',
    'contrary',
    'contrariwise',
    'controversial',
    'convenient',
    'converse',
    'convincing',
    'convivial',
    'convulsive',
    'cool',
    'cooperative',
    'copious',
    'cordial',
    'correct',
    'corrupt',
    'counterclockwise',
    'courageous',
    'courteous',
    'covert',
    'coward',
    'coy',
    'cozy',
    'crass',
    'craving',
    'crazy',
    'creative',
    'creditable',
    'criminal',
    'crisp',
    'critical',
    'crooked',
    'cross',
    'crosswise',
    'crude',
    'cruel',
    'cryptic',
    'cuddly',
    'cultural',
    'cunning',
    'curious',
    'cursory',
    'curt',
    'customary',
    'cute',
    'cynical',
    'daft',
    'daily',
    'dainty',
    'damnable',
    'dangerous',
    'daring',
    'dark',
    'dazzling',
    'defacto',
    'dead',
    'dear',
    'death',
    'decadent',
    'deceitful',
    'decent',
    'deceptive',
    'decided',
    'decisive',
    'declining',
    'deep',
    'defensive',
    'defiant',
    'definite',
    'deft',
    'degrading',
    'dejected',
    'deliberate',
    'deliberative',
    'delicate',
    'delicious',
    'delighted',
    'delightful',
    'delirious',
    'demanding',
    'demented',
    'democratic',
    'demographical',
    'demoniacal',
    'demoralizing',
    'demure',
    'dense',
    'denying',
    'deplorable',
    'depressed',
    'depressing',
    'depressive',
    'derisive',
    'deserved',
    'desirable',
    'desolate',
    'despairing',
    'desperate',
    'despicable',
    'despotic',
    'destructive',
    'determinative',
    'determined',
    'detrimental',
    'devastating',
    'devilish',
    'devious',
    'devoted',
    'devout',
    'dexterous',
    'diabolical',
    'diagonal',
    'different',
    'diffident',
    'diligent',
    'dim',
    'direct',
    'dirty',
    'disagreeable',
    'disagreeing',
    'disappointed',
    'disappointing',
    'disapproving',
    'disarming',
    'disastrous',
    'disbelieving',
    'discernible',
    'disconcerting',
    'disconnected',
    'disconsolate',
    'discontent',
    'discouraging',
    'discourteous',
    'discrete',
    'discriminating',
    'discursive',
    'disdainful',
    'disgraceful',
    'disgusted',
    'disgusting',
    'dishonest',
    'dishonorable',
    'dismal',
    'disparaging',
    'dispassionate',
    'disrespectful',
    'dissolute',
    'distant',
    'distinct',
    'distrustful',
    'disturbing',
    'diverse',
    'divine',
    'divisive',
    'dizzy',
    'dogmatic',
    'doleful',
    'dolorous',
    'domestic',
    'dominant',
    'dorsal',
    'dour',
    'doubtful',
    'doubtless',
    'downwards',
    'dramatic',
    'drastic',
    'dreadful',
    'dreamy',
    'dreary',
    'dry',
    'droll',
    'drowsy',
    'drunken',
    'dry',
    'dubious',
    'dull',
    'du',
    'dumb',
    'dutiful',
    'dying',
    'dynamic',
    'dyspeptic',
    'eager',
    'earnest',
    'easy',
    'eastwards',
    'eccentric',
    'economic',
    'ecstatic',
    'ecumenical',
    'editorial',
    'educational',
    'eerie',
    'effective',
    'effectual',
    'efficient',
    'effortless',
    'egocentric',
    'egoistic',
    'egotistic',
    'elaborate',
    'elder',
    'electrical',
    'electronic',
    'elegant',
    'eloquent',
    'elusive',
    'embarrassed',
    'eminent',
    'emotional',
    'emphatic',
    'empirical',
    'encouraging',
    'endearing',
    'endless',
    'enduring',
    'energetic',
    'engaging',
    'enigmatic',
    'enjoyable',
    'enormous',
    'enthusiastic',
    'entire',
    'enviable',
    'envious',
    'equable',
    'equal',
    'equitable',
    'equivocal',
    'erotic',
    'erratic',
    'erroneous',
    'essential',
    'eternal',
    'ethereal',
    'ethical',
    'ethnic',
    'evangelical',
    'evangelistic',
    'even',
    'eventual',
    'everlasting',
    'evident',
    'evil',
    'exact',
    'exceeding',
    'excellent',
    'exceptional',
    'excessive',
    'excited',
    'exclusive',
    'excruciating',
    'exhausted',
    'exhausting',
    'exotic',
    'expansive',
    'expectant',
    'expensive',
    'experimental',
    'expert',
    'explicit',
    'explosive',
    'express',
    'extemporaneous',
    'extensive',
    'external',
    'extortionate',
    'extraneous',
    'extravagant',
    'extrinsic',
    'exuberant',
    'exultant',
    'fabulous',
    'facetious',
    'fascinated',
    'factual',
    'faint',
    'fair',
    'faithful',
    'faithless',
    'false',
    'faltering',
    'familiar',
    'famous',
    'fanatical',
    'fanciful',
    'fancy',
    'fantastic',
    'fashionable',
    'fatal',
    'fateful',
    'father',
    'fatuous',
    'faulty',
    'faultless',
    'favorable',
    'fearful',
    'fearless',
    'feasible',
    'feeble',
    'feeling',
    'felicitous',
    'ferocious',
    'fervent',
    'fervid',
    'festive',
    'fetching',
    'feverish',
    'fiendish',
    'fierce',
    'fierce',
    'figurative',
    'final',
    'financial',
    'fine',
    'firm',
    'first',
    'fitful',
    'fit',
    'fitting',
    'fixed',
    'flagrant',
    'flamboyant',
    'flat',
    'flawless',
    'fleeting',
    'flexible',
    'flimsy',
    'flippant',
    'flirtatious',
    'flirting',
    'fluent',
    'foggy',
    'fond',
    'foolish',
    'forceful',
    'forcible',
    'forever',
    'forgetful',
    'forgiving',
    'forlorn',
    'formal',
    'formidable',
    'fortnight',
    'fortunate',
    'forwards',
    'foul',
    'fractal',
    'fragrant',
    'frank',
    'frantic',
    'fraternal',
    'fraudulent',
    'free',
    'frenetic',
    'frequent',
    'fresh',
    'fretful',
    'friendly',
    'friend',
    'frightened',
    'frightening',
    'frightful',
    'frivolous',
    'frugal',
    'full',
    'fundamental',
    'funny',
    'furious',
    'furtive',
    'fussy',
    'gay',
    'gallant',
    'game',
    'garrulous',
    'gaudy',
    'gay',
    'geekish',
    'general',
    'generous',
    'genetic',
    'genial',
    'gentle',
    'genuine',
    'ghastly',
    'ghost',
    'gigantic',
    'ginger',
    'girlish',
    'glad',
    'gleeful',
    'glib',
    'global',
    'gloomy',
    'glorious',
    'good-humored',
    'goofy',
    'gorgeous',
    'graceful',
    'gracious',
    'gradual',
    'grammatical',
    'grandfather',
    'grand',
    'grandmother',
    'graphical',
    'grateful',
    'grating',
    'grave',
    'great',
    'greedy',
    'gregarious',
    'grievous',
    'grim',
    'groovy',
    'gross',
    'grotesque',
    'gruesome',
    'gruff',
    'guiding',
    'guttural',
    'habitable',
    'habitual',
    'haggard',
    'halfhearted',
    'handy',
    'handsome',
    'haphazard',
    'hapless',
    'happy',
    'hard',
    'hardheaded',
    'hardhearted',
    'hardy',
    'hard',
    'harmful',
    'harmless',
    'harmonic',
    'harmonious',
    'harsh',
    'hasted',
    'hasty',
    'hateful',
    'haughty',
    'haunting',
    'hazy',
    'healthful',
    'healthy',
    'heartbroken',
    'hearty',
    'heartwarming',
    'heated',
    'heaven',
    'heavy',
    'hectic',
    'heedful',
    'heedless',
    'heinous',
    'hellish',
    'helpful',
    'helpless',
    'heroic',
    'hesitant',
    'heterogeneous',
    'hideous',
    'higgledy-piggledy',
    'hilarious',
    'historical',
    'histrionic',
    'hoarse',
    'hollow',
    'honest',
    'honorable',
    'honorary',
    'hopeful',
    'hopeless',
    'horizontal',
    'horny',
    'horrible',
    'horrid',
    'horrifying',
    'hospitable',
    'hostile',
    'hotheaded',
    'hot',
    'hour',
    'housewife',
    'howsoever',
    'hubwards',
    'huge',
    'humane',
    'human',
    'humble',
    'humid',
    'humorless',
    'humorous',
    'humorless',
    'hungry',
    'hurried',
    'husky',
    'hygienic',
    'hypercritical',
    'hypnotic',
    'hypocritical',
    'hypothetical',
    'hysterical',
    'icy',
    'ideal',
    'idiotic',
    'idle',
    'ignoble',
    'ignominious',
    'ignorant',
    'ill-advised',
    'ill-natured',
    'illegal',
    'illegible',
    'illegitimate',
    'illicit',
    'illogical',
    'illustrative',
    'imaginable',
    'imaginative',
    'immaculate',
    'immeasurable',
    'immediate',
    'immense',
    'imminent',
    'immoderate',
    'immodest',
    'immoral',
    'immortal',
    'immovable',
    'immutable',
    'impartial',
    'impassive',
    'impatient',
    'impeccable',
    'impenetrable',
    'imperative',
    'imperceptible',
    'imperfect',
    'imperious',
    'impermanent',
    'impersonal',
    'impertinent',
    'impetuous',
    'impish',
    'implacable',
    'implicit',
    'impolite',
    'important',
    'impossible',
    'impotent',
    'impressive',
    'improbable',
    'improper',
    'impudent',
    'impulsive',
    'inadequate',
    'inadvertent',
    'inalienable',
    'inane',
    'inappreciable',
    'inarticulate',
    'inaudible',
    'incalculable',
    'incessant',
    'incidental',
    'incisive',
    'incoherent',
    'incommunicado',
    'incomplete',
    'incongruous',
    'inconsequential',
    'inconsiderate',
    'inconsolable',
    'inconspicuous',
    'inconstant',
    'incontestable',
    'incontrollable',
    'incontrovertible',
    'inconvenient',
    'incorporeal',
    'incorrect',
    'incorrigible',
    'incorruptible',
    'increasing',
    'incredible',
    'incredulous',
    'indecent',
    'indecisive',
    'indecorous',
    'indeed',
    'indefatigable',
    'indefeasible',
    'indefinite',
    'indelible',
    'independent',
    'indescribable',
    'indeterminate',
    'indifferent',
    'indignant',
    'indirect',
    'indiscriminate',
    'indispensable',
    'indisputable',
    'indistinct',
    'individual',
    'indivisible',
    'indolent',
    'indomitable',
    'indubitable',
    'indulgent',
    'industrial',
    'industrious',
    'ineffable',
    'ineffective',
    'ineffectual',
    'inefficient',
    'inept',
    'inert',
    'inescapable',
    'inestimable',
    'inevitable',
    'inexact',
    'inexcusable',
    'inexhaustible',
    'inexorable',
    'inexpert',
    'inexplicable',
    'inexpressible',
    'inextricable',
    'infallible',
    'infamous',
    'inferior',
    'infernal',
    'infinite',
    'infinitesimal',
    'inflexible',
    'informal',
    'infrequent',
    'ingenious',
    'ingenuous',
    'inglorious',
    'inherent',
    'inhospitable',
    'inhuman',
    'inimical',
    'initial',
    'innate',
    'innocent',
    'innocuous',
    'inopportune',
    'inordinate',
    'inquiring',
    'inquisitive',
    'insane',
    'inscrutable',
    'insecure',
    'insensible',
    'inseparable',
    'insincere',
    'insistent',
    'insolent',
    'insolvable',
    'instantaneous',
    'instant',
    'instead',
    'instinctive',
    'institutional',
    'insufferable',
    'insufficient',
    'insuperable',
    'intangible',
    'intellectual',
    'intelligent',
    'intelligible',
    'intend',
    'intense',
    'intensive',
    'intensive',
    'intentional',
    'intent',
    'interactive',
    'interested',
    'interesting',
    'interminable',
    'intermittent',
    'internal',
    'international',
    'intimate',
    'intolerable',
    'intransitive',
    'intravenous',
    'intricate',
    'intriguing',
    'intrinsic',
    'introspective',
    'intuitive',
    'invariable',
    'inverse',
    'invidious',
    'invincible',
    'invisible',
    'inviting',
    'involuntary',
    'invulnerable',
    'inward',
    'irate',
    'irksome',
    'ironic',
    'irrational',
    'irregular',
    'irresistible',
    'irresistible',
    'irresolute',
    'irresponsible',
    'irritated',
    'irrevocable',
    'irritable',
    'irritating',
    'jealous',
    'jeering',
    'jerky',
    'joint',
    'joking',
    'jovial',
    'joyful',
    'joyous',
    'jubilant',
    'judicial',
    'judicious',
    'just',
    'keen',
    'kidding',
    'kind',
    'knowing',
    'laborious',
    'lackadaisical',
    'laconic',
    'lambent',
    'lame',
    'lamentable',
    'languid',
    'languorous',
    'large',
    'last',
    'late',
    'lateral',
    'latter',
    'laudable',
    'lavish',
    'lawful',
    'lax',
    'lazy',
    'leeward',
    'leftist',
    'legal',
    'legible',
    'legitimate',
    'leisure',
    'lengthwise',
    'lenient',
    'lethal',
    'level',
    'lewd',
    'liberal',
    'licentious',
    'lighthearted',
    'light',
    'likewise',
    'limp',
    'listless',
    'literal',
    'liturgical',
    'live',
    'local',
    'lofty',
    'logical',
    'lone',
    'long',
    'longing',
    'longitudinal',
    'loose',
    'lopsided',
    'loud',
    'lousy',
    'loutish',
    'lovable',
    'loving',
    'low',
    'loyal',
    'lucid',
    'lucky',
    'lucrative',
    'ludicrous',
    'lugubrious',
    'luminous',
    'lurid',
    'luscious',
    'lustful',
    'lusty',
    'luxuriant',
    'luxurious',
    'mad',
    'magical',
    'magnanimous',
    'magnetic',
    'magnificent',
    'main',
    'majestic',
    'malapropos',
    'malevolent',
    'malicious',
    'malignant',
    'malodorous',
    'manageable',
    'manful',
    'maniacal',
    'maniacal',
    'manifest',
    'mannish',
    'manual',
    'manifold',
    'marked',
    'marvelous',
    'masochistic',
    'massive',
    'masterful',
    'materialistic',
    'maternal',
    'mathematical',
    'matrimonial',
    'matter-of-fact',
    'mawkish',
    'maximal',
    'meager',
    'meaningful',
    'meaningless',
    'meaning',
    'mean',
    'measurable',
    'mechanical',
    'mechanistic',
    'medical',
    'medicinal',
    'medieval',
    'meditative',
    'meek',
    'melancholic',
    'mellifluous',
    'melodic',
    'melodious',
    'melting',
    'memorable',
    'menacing',
    'mendacious',
    'menial',
    'mental',
    'mercenary',
    'merciful',
    'merciless',
    'mercurial',
    'mere',
    'meretricious',
    'meritorious',
    'merry',
    'metaphorical',
    'methodical',
    'meticulous',
    'metrical',
    'microscopical',
    'midweek',
    'mighty',
    'mighty',
    'mild',
    'militant',
    'militaristic',
    'mindful',
    'minute',
    'miraculous',
    'mirthful',
    'misanthropic',
    'miscellaneous',
    'mischievous',
    'miserable',
    'misguiding',
    'mistaken',
    'misty',
    'mistrustful',
    'mocking',
    'moderate',
    'modern',
    'modest',
    'modish',
    'moist',
    'momentary',
    'momentous',
    'monastic',
    'monkish',
    'monosyllabic',
    'monotonous',
    'monstrous',
    'month',
    'monumental',
    'moody',
    'moralistic',
    'moral',
    'morbid',
    'mordant',
    'moronic',
    'morose',
    'mortal',
    'most',
    'mother',
    'motionless',
    'mournful',
    'muddy',
    'mulish',
    'multifarious',
    'mundane',
    'municipal',
    'murderous',
    'murky',
    'musical',
    'musing',
    'mussy',
    'musty',
    'mutable',
    'mutational',
    'mute',
    'mutinous',
    'mutual',
    'myopic',
    'mysterious',
    'mystical',
    'naive',
    'naked',
    'nameless',
    'name',
    'narrow',
    'nasal',
    'nasty',
    'national',
    'natty',
    'natural',
    'naughty',
    'nauseating',
    'nauseous',
    'nautical',
    'nearby',
    'near',
    'necessary',
    'needless',
    'nefarious',
    'negative',
    'negligent',
    'neonatal',
    'nerdish',
    'nervous',
    'nevermore',
    'nevertheless',
    'nice',
    'nimble',
    'nob',
    'nocturnal',
    'noiseless',
    'noisy',
    'nominal',
    'nonchalant',
    'nonetheless',
    'nonstop',
    'normal',
    'northeastwards',
    'northwards',
    'northwestwards',
    'nostalgic',
    'notable',
    'noticeable',
    'notorious',
    'numb',
    'numerical',
    'obedient',
    'objective',
    'obliging',
    'oblique',
    'oblivious',
    'obnoxious',
    'obscene',
    'obscure',
    'obsequious',
    'obstinate',
    'obtuse',
    'obverse',
    'obvious',
    'occasional',
    'occupational',
    'octagonal',
    'odd',
    'odious',
    'offensive',
    'offhand',
    'official',
    'officious',
    'often',
    'ominous',
    'ominous',
    'omnipotent',
    'omniscient',
    'omnivorous',
    'once',
    'opaque',
    'open',
    'opportune',
    'opposite',
    'oppressive',
    'opprobrious',
    'optimal',
    'optimistic',
    'ordinary',
    'organic',
    'original',
    'ornate',
    'orthodox',
    'orthogonal',
    'ostensible',
    'ostentatious',
    'otherwise',
    'outrageous',
    'outright',
    'outward',
    'over',
    'over',
    'owlish',
    'painful',
    'painstaking',
    'palpable',
    'paradoxical',
    'parenthetical',
    'parlous',
    'parsimonious',
    'partial',
    'particular',
    'part',
    'passable',
    'passionate',
    'passive',
    'paternal',
    'pathetic',
    'patient',
    'patriotic',
    'patronizing',
    'peaceable',
    'peaceful',
    'peculiar',
    'peevish',
    'pensive',
    'perceptible',
    'perceptive',
    'perceptual',
    'peremptory',
    'perfect',
    'perfunctory',
    'perilous',
    'periodic',
    'permanent',
    'perpendicular',
    'perpetual',
    'perplexed',
    'persistent',
    'personable',
    'personal',
    'persuasive',
    'perverse',
    'perverted',
    'petty',
    'petulant',
    'philosophical',
    'physical',
    'physiological',
    'piggyback',
    'pious',
    'piteous',
    'pitiful',
    'placid',
    'plain',
    'plaintive',
    'playbill',
    'playful',
    'pleasant',
    'pleasing',
    'pleasurable',
    'plentiful',
    'plush',
    'pointed',
    'pointless',
    'polite',
    'political',
    'pompous',
    'ponderous',
    'poor',
    'popular',
    'pornographic',
    'positive',
    'possessive',
    'possible',
    'potential',
    'potent',
    'powerful',
    'powerless',
    'practical',
    'prayerful',
    'precarious',
    'precipitate',
    'precipitous',
    'precise',
    'precocious',
    'preconceived',
    'predisposing',
    'preeminent',
    'preferable',
    'premature',
    'present',
    'presumable',
    'pretentious',
    'pretty',
    'previous',
    'priggish',
    'primary',
    'principal',
    'private',
    'privy',
    'probable',
    'profane',
    'professed',
    'professional',
    'proficient',
    'profitable',
    'profligate',
    'profound',
    'profuse',
    'progressive',
    'prohibitory',
    'prolific',
    'prominent',
    'promiscuous',
    'promising',
    'prompt',
    'pronto',
    'proper',
    'prophetic',
    'proportionate',
    'prospective',
    'protective',
    'proud',
    'provident',
    'provocative',
    'prudent',
    'psychic',
    'psychological',
    'public',
    'punctual',
    'pungent',
    'pure',
    'purposeful',
    'purpose',
    'puzzled',
    'quaint',
    'qualitative',
    'quantitative',
    'queer',
    'questioning',
    'quibbling',
    'quick',
    'quiet',
    'quizzical',
    'quotable',
    'rabid',
    'racy',
    'radial',
    'radiant',
    'radical',
    'ragged',
    'rakish',
    'rampant',
    'random',
    'rank',
    'rapacious',
    'rapid',
    'rapt',
    'rare',
    'rash',
    'rational',
    'raucous',
    'ravenous',
    'readable',
    'ready',
    'realistic',
    'real',
    'reasonable',
    'reassuring',
    'rebellious',
    'recent',
    'receptive',
    'reciprocal',
    'reckless',
    'recognizable',
    'recursive',
    'red-handed',
    'red',
    'redolent',
    'redundant',
    'reflexive',
    'reflex',
    'refractory',
    'refreshing',
    'regal',
    'regional',
    'regretful',
    'regrettable',
    'regular',
    'relative',
    'relentless',
    'relevant',
    'reliable',
    'religious',
    'reluctant',
    'remarkable',
    'remedial',
    'reminiscent',
    'remiss',
    'remonstrant',
    'remote',
    'remunerative',
    'repeated',
    'repetitious',
    'repetitive',
    'reported',
    'reprehensible',
    'representative',
    'reproachful',
    'repugnant',
    'repulsive',
    'reputable',
    'reputed',
    'resentful',
    'reserved',
    'residential',
    'resigned',
    'resistant',
    'resolute',
    'resonant',
    'resounding',
    'respectable',
    'respectful',
    'respective',
    'resplendent',
    'responsible',
    'responsive',
    'restful',
    'restive',
    'restless',
    'restrained',
    'restrictive',
    'reticent',
    'retrospective',
    'reverent',
    'reverse',
    'revolting',
    'rhapsodic',
    'rhythmic',
    'rich',
    'ridiculous',
    'right-handed',
    'righteous',
    'rightful',
    'right',
    'rigid',
    'rigorous',
    'rigorous',
    'rimwards',
    'ripe',
    'ritualistic',
    'robust',
    'roguish',
    'rollicking',
    'romantic',
    'rosy',
    'rough',
    'roughshod',
    'round',
    'routine',
    'royal',
    'rude',
    'rueful',
    'ruffian',
    'rugged',
    'ruinous',
    'rustic',
    'ruthless',
    'rhythmic',
    'sacerdotal',
    'sacred',
    'sacrificial',
    'sacrilegious',
    'sadistic',
    'sad',
    'safe',
    'sage',
    'saint',
    'sanctimonious',
    'sane',
    'sarcastic',
    'sardonic',
    'satanic',
    'satirical',
    'saucy',
    'savage',
    'scandalous',
    'scanty',
    'scarce',
    'skeptical',
    'scientific',
    'scornful',
    'scriptural',
    'scrumdiddumptious',
    'scrumptious',
    'scrupulous',
    'scurvy',
    'searching',
    'searing',
    'second',
    'secretive',
    'secret',
    'secure',
    'sedate',
    'seductive',
    'seeming',
    'seismic',
    'seldom',
    'self-conscious',
    'selfish',
    'sensational',
    'sensible',
    'sensitive',
    'sensual',
    'sensuous',
    'sentimental',
    'separate',
    'separatist',
    'serene',
    'serious',
    'several',
    'severe',
    'sexy',
    'sexual',
    'shaky',
    'shallow',
    'shamefaced',
    'shameful',
    'shameless',
    'shapeless',
    'sharp',
    'sheepish',
    'shocking',
    'shoddy',
    'short',
    'showy',
    'shrewd',
    'shrill',
    'shy',
    'sick',
    'sideways',
    'signal',
    'significant',
    'silent',
    'silly',
    'similar',
    'simpering',
    'simultaneous',
    'sincere',
    'sinful',
    'sing',
    'singular',
    'sister',
    'sizable',
    'skeptical',
    'skillful',
    'skyward',
    'slack',
    'slanting',
    'slantwise',
    'slattern',
    'slavish',
    'sleepy',
    'slight',
    'sloppy',
    'slow',
    'sluggish',
    'sly',
    'smart',
    'smiling',
    'smooth',
    'smug',
    'snappy',
    'sneak',
    'sneaking',
    'snide',
    'sniffing',
    'snobbish',
    'snug',
    'sober',
    'sociable',
    'social',
    'soft',
    'soggy',
    'soldier',
    'sole',
    'solemn',
    'solicitous',
    'solid',
    'somber',
    'someday',
    'somehow',
    'sometimes',
    'soothing',
    'sordid',
    'sore',
    'sorrowful',
    'sortof',
    'soothing',
    'soulful',
    'sound',
    'sour',
    'southeastwards',
    'southwards',
    'southwestwards',
    'spacious',
    'sparing',
    'sparse',
    'spasmodic',
    'spastic',
    'spatial',
    'special',
    'specific',
    'spectacular',
    'speculative',
    'speedy',
    'spherical',
    'spinal',
    'spiral',
    'spiritual',
    'spiteful',
    'splendid',
    'spontaneous',
    'sporadic',
    'sporting',
    'spotless',
    'square',
    'stalwart',
    'stark',
    'staunch',
    'steadfast',
    'steady',
    'steady',
    'stealthy',
    'steep',
    'stern',
    'stiff',
    'stoic',
    'stolid',
    'stony',
    'stormy',
    'stout',
    'straightforward',
    'strange',
    'strenuous',
    'strict',
    'striking',
    'strong',
    'stubborn',
    'studious',
    'stunning',
    'stupendous',
    'stupid',
    'sturdy',
    'stylish',
    'suave',
    'subconscious',
    'subjective',
    'submissive',
    'subsequent',
    'substantial',
    'subtle',
    'successful',
    'successive',
    'succinct',
    'sudden',
    'suffering',
    'sufficient',
    'suggestive',
    'suicidal',
    'suitable',
    'sulky',
    'sullen',
    'summary',
    'superb',
    'supercilious',
    'superficial',
    'superfluous',
    'supernatural',
    'supporting',
    'supportive',
    'supposed',
    'supreme',
    'sure',
    'surgical',
    'surprising',
    'surreptitious',
    'suspicious',
    'sweet',
    'swift',
    'symbolic',
    'symmetric',
    'sympathetic',
    'synergistic',
    'synthetic',
    'systematic',
    'tacit',
    'tactful',
    'tactless',
    'talkative',
    'tame',
    'tantalizing',
    'tardy',
    'tart',
    'tasteful',
    'tasteless',
    'taunting',
    'taut',
    'tawdry',
    'tearful',
    'teasing',
    'technical',
    'tedious',
    'telepathic',
    'tempestuous',
    'temporary',
    'temporarily',
    'tenacious',
    'tender',
    'tense',
    'tentative',
    'tenuous',
    'terminal',
    'terrible',
    'terrific',
    'terrifying',
    'terse',
    'testing',
    'thankful',
    'theatric',
    'theological',
    'theoretical',
    'therapeutic',
    'thermodynamic',
    'thick',
    'thin',
    'thorough',
    'thoughtful',
    'thoughtless',
    'threatening',
    'threefold',
    'thrice',
    'thrifty',
    'throaty',
    'thunderous',
    'tight',
    'timeless',
    'timid',
    'timorous',
    'tired',
    'tireless',
    'tiresome',
    'tiring',
    'tolerable',
    'tolerant',
    'topical',
    'topsy-turvy',
    'total',
    'tough',
    'traditional',
    'tragic',
    'tranquil',
    'transcendental',
    'transient',
    'transitive',
    'transparent',
    'transverse',
    'treacherous',
    'tremendous',
    'tremulous',
    'triangular',
    'trim',
    'triumphant',
    'troublesome',
    'truculent',
    'true',
    'trustful',
    'trusting',
    'truthful',
    'tuneful',
    'turbulent',
    'turnwise',
    'twice',
    'two-faced',
    'typical',
    'typographical',
    'tyrannical',
    'tyrannous',
    'ubiquitous',
    'ultimate',
    'unaccountable',
    'unadvised',
    'unaffected',
    'unanimous',
    'unattractive',
    'unavailing',
    'unavoidable',
    'unabashed',
    'unbearable',
    'unbecoming',
    'unbelievable',
    'unblushing',
    'uncanny',
    'unceasing',
    'unceremonious',
    'uncertain',
    'uncharitable',
    'unchaste',
    'uncomfortable',
    'uncommon',
    'unconcerned',
    'unconditional',
    'unconscionable',
    'unconscious',
    'unconstitutional',
    'uncontrollable',
    'unconventional',
    'uncritical',
    'unctuous',
    'undaunted',
    'undead',
    'undeniable',
    'underhanded',
    'understandable',
    'understanding',
    'undetermined',
    'undoubted',
    'undramatic',
    'undue',
    'uneasy',
    'unequal',
    'unequivocal',
    'unerring',
    'uneven',
    'unexpected',
    'unfair',
    'unfaithful',
    'unfavorable',
    'unfeeling',
    'unforgettable',
    'unfortunate',
    'ungraceful',
    'ungrateful',
    'unhappy',
    'uniform',
    'unilateral',
    'unintelligible',
    'unintentional',
    'universal',
    'unjust',
    'unkind',
    'unknowing',
    'unlawful',
    'unlike',
    'unlucky',
    'unmannered',
    'unmistakable',
    'unnatural',
    'unnecessary',
    'unpleasant',
    'unpalatable',
    'unpredictable',
    'unqualified',
    'unquestionable',
    'unquestioning',
    'unreasonable',
    'unrelenting',
    'unremitting',
    'unreserved',
    'unseasonable',
    'unselfish',
    'unsound',
    'unspeakable',
    'unsteady',
    'unsuccessful',
    'unsuitable',
    'unthinking',
    'unusual',
    'unutterable',
    'unwilling',
    'unwise',
    'unwitting',
    'unwonted',
    'uppermost',
    'upright',
    'uproarious',
    'upsidedown',
    'upwards',
    'urgent',
    'useful',
    'useless',
    'usual',
    'utter',
    'vacant',
    'vagrant',
    'vague',
    'vain',
    'valiant',
    'valid',
    'vanward',
    'vapid',
    'vaporous',
    'variable',
    'varied',
    'varietal',
    'various',
    'vast',
    'vehement',
    'venal',
    'vengeful',
    'venomous',
    'ventral',
    'venturesome',
    'venturous',
    'veracious',
    'verbal',
    'verbatim',
    'verdant',
    'very',
    'veritable',
    'vertical',
    'vestal',
    'vestigial',
    'vexatious',
    'viable',
    'vicarious',
    'vicious',
    'victorious',
    'vigilant',
    'vigorous',
    'vile',
    'villainous',
    'vindictive',
    'violent',
    'virginal',
    'virtual',
    'virtuous',
    'virulent',
    'visceral',
    'viscid',
    'visible',
    'visual',
    'vital',
    'vituperative',
    'vivacious',
    'vivid',
    'vociferous',
    'voiceless',
    'voluble',
    'voluminous',
    'voluntary',
    'voluptuous',
    'voracious',
    'vulgar',
    'vulnerable',
    'wakeful',
    'wane',
    'wanton',
    'wary',
    'warm',
    'warning',
    'wasteful',
    'watchful',
    'wavelength',
    'wavering',
    'weak',
    'weary',
    'wearisome',
    'week',
    'weird',
    'westwards',
    'wet',
    'whimsical',
    'wholehearted',
    'whole',
    'wicked',
    'widdershins',
    'wide',
    'wild',
    'willful',
    'willing',
    'wimpy',
    'winsome',
    'wise',
    'wishful',
    'wistful',
    'withal',
    'witless',
    'witting',
    'wobbly',
    'woeful',
    'wolfish',
    'wonderful',
    'wondering',
    'wondrous',
    'wooden',
    'worrying',
    'worthy',
    'wrathful',
    'wrinkled',
    'wrong',
    'wrong',
    'wry',
    'xenophobic',
    'yearning',
    'yellowish',
    'youthful',
    'zany',
    'zealous',
    'zen-like',
    'zestful',
    'zonal',
    'zoological',
]

print " ".join([adjectives[random.randrange(0, len(adjectives))] for i in range(10)])