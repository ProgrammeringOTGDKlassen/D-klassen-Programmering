import datetime

class Subject:
	"""
	Represents a Subject type; does NOT represent a row in the 'subjects' table.
	"""

	DANSK = 0
	MATEMATIK = 1
	FYSIK = 2
	KEMI = 3
	BIOLOGI = 4
	SAMFUNDSFAG = 5
	KOMIT = 6
	MEDIEFAG = 7
	TYSK = 8
	ERHVERSOEKONOMI = 9
	IDEHISTORIE = 10
	PROGRAMMERING = 11
	TEKNOLOGI = 12
	BIOTEKNOLOGI = 13
	DESIGN = 14
	PSYKOLOGI = 15
	FILOSOFI = 16
	STATIK = 17
	ASTRONOMI = 18
	IDRAET = 19
	ANDENUNDERVISNING = 20
	ENGELSK = 21
	NV_GRUNDFORLOEB = 22
	PU_GRUNDFORLOEB = 23
	INNOVATION = 24
	INTERNATIONAL_TEK_OG_KULTUR = 25
	TEKNIK_EL = 26
	TEKNIK_BYG = 27
	TEKNIK_PROCES = 28
	TEKNIK_TEKSTIL = 29
	TEKNIK_MASKIN = 30

	# Subject name strings
	SUBJECTS = {
		DANSK: "Dansk",
		MATEMATIK: "Matematik",
		FYSIK: "Fysik",
		KEMI: "Kemi",
		BIOLOGI: "Biologi",
		SAMFUNDSFAG: "Samfundsfag",
		KOMIT: "Kommunikation og IT",
		MEDIEFAG: "Mediefag",
		TYSK: "Tysk",
		ERHVERSOEKONOMI: "Erhvervsøkonomi",
		IDEHISTORIE: "Idehistorie",
		PROGRAMMERING: "Programmering",
		TEKNOLOGI: "Teknologi",
		BIOTEKNOLOGI: "Bioteknologi",
		DESIGN: "Design",
		PSYKOLOGI: "Psykologi",
		FILOSOFI: "Filosofi",
		STATIK: "Statik og styrkelære",
		ASTRONOMI: "Astronomi",
		IDRAET: "Idræt",
		ANDENUNDERVISNING: "Anden UV",
		ENGELSK: "Engelsk",
		NV_GRUNDFORLOEB: "Naturvidenskabeligt grundforløb",
		PU_GRUNDFORLOEB: "Produktudvikling",
		INNOVATION: "Innovation",
		INTERNATIONAL_TEK_OG_KULTUR: "International teknologi og kultur",
		TEKNIK_EL: "El-teknikfag",
		TEKNIK_BYG: "Byg-teknikfag",
		TEKNIK_PROCES: "Proces-teknikfag",
		TEKNIK_TEKSTIL: "Tekstil-teknikfag",
		TEKNIK_MASKIN: "Maskin-teknikfag"
	}

	# Subject short-name strings
	SHORTNAME = {
		DANSK: "Dan",
		MATEMATIK: "Mat",
		FYSIK: "Fys",
		KEMI: "Kem",
		BIOLOGI: "Bio",
		SAMFUNDSFAG: "Sam",
		KOMIT: "K/IT",
		MEDIEFAG: "Med",
		TYSK: "Tysk",
		ERHVERSOEKONOMI: "Erhv",
		IDEHISTORIE: "Idehi",
		PROGRAMMERING: "Prg",
		TEKNOLOGI: "Tek",
		BIOTEKNOLOGI: "Biotk",
		DESIGN: "Desn",
		PSYKOLOGI: "Psy",
		FILOSOFI: "Fil",
		STATIK: "Stati",
		ASTRONOMI: "Astr",
		IDRAET: "Idræ",
		ANDENUNDERVISNING: "And. uv.",
		ENGELSK: "Eng",
		NV_GRUNDFORLOEB: "NV",
		PU_GRUNDFORLOEB: "PU",
		INNOVATION: "Inno",
		INTERNATIONAL_TEK_OG_KULTUR: "Int. t/k",
		TEKNIK_EL: "Elt",
		TEKNIK_BYG: "Byg",
		TEKNIK_PROCES: "Proc",
		TEKNIK_TEKSTIL: "Teks",
		TEKNIK_MASKIN: "Maski"
	}

	@staticmethod
	def name(subject):
		return Subject.SUBJECTS[subject]

	@staticmethod
	def shortName(subject):
		return Subject.SHORTNAME[subject]

class SubjectLevel:
	"""
	Level of a subject: A, B, C.
	"""

	C = 0
	B = 1
	A = 2

	SUBJECTLEVELS = {
		C: "C",
		B: "B",
		A: "A"
	}

	@staticmethod
	def name(subjectLevel):
		return SubjectLevel.SUBJECTLEVELS[subjectLevel]

class GradeType:
	"""
	The type of grade given.
	"""

	WRITTEN = 0
	ORAL = 1
	TOTAL = 2

	GRADETYPES = {
		WRITTEN: "Skriftlig",
		ORAL: "Mundtlig",
		TOTAL: "Helhedsvurdering"
	}

	SHORTGRADETYPES = {
		WRITTEN: "Skr.",
		ORAL: "Mdt.",
		TOTAL: "Helh."
	}

	@staticmethod
	def name(type):
		return GradeType.GRADETYPES[type]

	@staticmethod
	def shortName(type):
		return GradeType.SHORTGRADETYPES[type]

class UserType:
	STUDENT = 0
	TEACHER = 1
	ADMINISTRATOR = 2

	USERTYPES = {
		STUDENT: "Elev",
		TEACHER: "Lærer",
		ADMINISTRATOR: "Administrator"
	}

	@staticmethod
	def name(type):
		return UserType.USERTYPES[type]

class TaskType:
	"""
	The type of a task
	"""

	READ = 0
	SUBMISSION = 1
	OTHER = 2

	TASKTYPES = {
		READ: "Læs",
		SUBMISSION: "Aflevering",
		OTHER: "Andet"
	}

	@staticmethod
	def name(type):
		return TaskType.TASKTYPES[type]

class StudyLine:
	"""
	Line of study
	"""

	MAT_BIO = 0
	MAT_FYS = 1
	MAT_PROG = 2
	MAT_KEMI = 3
	MAT_BIOTEK = 4
	MAT_TEKN = 5

	BIOTEK_IDRAET = 6

	TEK_DESIGN = 7

	KIT_SAMF = 8
	KIT_PROG = 9
	KIT_DESIGN = 10

	# Lavet for at kunne oprette grundforløbsklasserne
	INGEN = 11

	STUDYLINES = {
		MAT_BIO: "Matematik A - Biologi B",
		MAT_FYS: "Matematik A - Fysik A",
		MAT_PROG: "Matematik A - Programmering B",
		MAT_KEMI: "Matematik A - Kemi A",
		MAT_BIOTEK: "Matematik A - Bioteknologi A",

		BIOTEK_IDRAET: "Bioteknologi A - Idræt B",

		TEK_DESIGN: "Teknologi A - Design B",

		KIT_SAMF: "Kommunikation & IT A - Samfundsfag B",
		KIT_PROG: "Kommunikation & IT A - Programmering B",
		KIT_DESIGN: "Kommunikation & IT A - Design B",

		INGEN: "Ingen Studieretning"
	}

	@staticmethod
	def name(studyline):
		return StudyLine.STUDYLINES[studyline]

def formatGraduationYear(year):
	"""
	Returns the formatted year of a class.\nE.g. current year: 2020 | input: 2020, output: 3
	"""
	# Retrieve current year
	nowYear = datetime.datetime.now().year

	# Årgangen som de går på: (1. g, 2.g, 3. g)
	return nowYear - year + 3

def isInt(s):
	"""
	Return true if given value is an int, otherwise false.
	"""
	try:
		int(s)
		return True
	except:
		return False

if __name__ == "__main__":
	print(Subject.name(Subject.ASTRONOMI))
