from flask import (
    Flask,
    request,
    g,
    render_template,
    session,
    redirect,
    url_for,
    send_file,
)

# !
# ! https://stackoverflow.com/questions/49921721/runtimeerror-main-thread-is-not-in-main-loop-with-matplotlib-and-flask
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

# !
import io
from random import randint, uniform
from math import tan, radians, dist, sqrt, pi

app = Flask(__name__)
app.secret_key = "very secret string"

answers = {}


def my_render(template, **kwargs):
    return render_template(template, **kwargs)


@app.route("/")
@app.route("/home")
def home():
    return my_render("home.html")


@app.route("/geometri")
def geometri():
    return my_render("geometri.html", title="Klassisk geometri")


@app.route("/analgeo")
def analgeo():
    return my_render("analytiskgeo.html", title="Analytisk geometri")


@app.route("/opg", methods=["GET"])
def opg():
    opg_id = int(request.args["opg_id"])
    if opg_id == 1:
        return generate_skaering_to_linjer()
    if opg_id == 2:
        pass
    if opg_id == 3:
        return generate_two_circle_intersect()
    if opg_id == 4:
        return generate_circular_arc()
    else:
        print("Stor gay")


@app.route("/submit_answer", methods=["POST"])
def submit_answer():
    question_id = request.args["qid"]
    svar = request.form["svar"]
    opgave_id = request.args["oid"]

    if answers[question_id] == svar:
        result = True
    else:
        result = False
    return my_render("result.html", result=result, return_opg=opgave_id)


def register_answer(answer):
    id = str(len(answers.keys()))
    answers[id] = answer
    return id


def generate_skaering_to_linjer():
    # Vælg et skæringspunkt:
    x = randint(-9, 9)
    y = randint(-9, 9)
    # Vælg en retning for p:
    a1 = tan(radians(randint(0, 89)))
    # Vælg en retning for q:
    a2 = tan(radians(randint(91, 179)))
    # Bestem b1
    b1 = y - a1 * x
    # Bestem b2
    b2 = y - a2 * x
    # Question id bruges til at tjekke resultatet senere.
    qid = register_answer("({},{})".format(x, y))
    return my_render(
        "skaeringtolinjer.html",
        title="Skæring mellem to linjer",
        opg_id=qid,
        a1=a1,
        a2=a2,
        b1=b1,
        b2=b2,
    )


def get_circle_radius(cent1, cent2, distance):
    r1 = uniform(1, distance)
    r2 = uniform(1, (r1 + distance))
    rdist = r1 + r2
    # * checks
    while not rdist >= distance:
        r2 = uniform(1, (r1 + distance))
        rdist = r1 + r2
    if r1 > r2 + distance or r2 > r1 + distance:
        raise ValueError("Radius too long")
    if not r1 >= 1 or not r1 >= 1:
        raise ValueError("Radius not at least 1")
    return (r1, r2)


def get_intercetions(x0, y0, r0, x1, y1, r1):
    # circle 1: (x0, y0), radius r0
    # circle 2: (x1, y1), radius r1

    # The afstandsformel
    d = sqrt((x1 - x0) ** 2 + (y1 - y0) ** 2)

    # non intersecting
    if d > r0 + r1:
        return None
    # One circle within other
    if d < abs(r0 - r1):
        return None
    # coincident circles
    if d == 0 and r0 == r1:
        return None
    if d == r0 + r1:
        # vector1 = (x0, y0)
        # vector2 = (x1, y1)
        x3, y3 = (((x1 - x0) / 2) + x0, ((y1 - y0) / 2) + y0)
        x4, y4 = None, None
    if (d + r1) == r0:
        x3, y3 = (((x1 - x0) / d) * r0, (((x1 - x0)) / d) * r0)
        x4, y4 = None, None
    if (d + r0) == r1:
        x3, y3 = (((x0 - x1) / d) * r1, (((x0 - x1)) / d) * r1)
        x4, y4 = None, None
    else:
        a = (r0 ** 2 - r1 ** 2 + d ** 2) / (2 * d)
        h = sqrt(r0 ** 2 - a ** 2)
        x2 = x0 + a * (x1 - x0) / d
        y2 = y0 + a * (y1 - y0) / d
        x3 = x2 + h * (y1 - y0) / d
        y3 = y2 - h * (x1 - x0) / d

        x4 = x2 - h * (y1 - y0) / d
        y4 = y2 + h * (x1 - x0) / d

        return (x3, y3, x4, y4)


def generate_two_circle_intersect():
    # Generate 2 points (x:[-40;40], y:[-40;40]) (center)
    c1x, c1y = (randint(-40, 40), randint(-40, 40))
    c2x, c2y = (randint(-40, 40), randint(-40, 40))
    cent1, cent2 = ([c1x, c1y], [c2x, c2y])

    # Calc dist between points
    distance = dist(cent1, cent2)

    c1r, c2r = get_circle_radius(cent1, cent2, distance)

    x1, y1, x2, y2 = get_intercetions(c1x, c1y, c1r, c2x, c2y, c2r)

    two_points = True
    if x2 == None or y2 == None:
        two_points = False

    if two_points:
        x1, y1, x2, y2 = (round(x1, 2), round(y1, 2), round(x2, 2), round(y2, 2))
        qid = register_answer("({},{}), ({},{})".format(x1, y1, x2, y2))
    else:
        x1, y1 = (round(x1, 2), round(y1, 2))
        qid = register_answer("({},{})".format(x1, y1))

    return my_render(
        "intersecttwocircle.html",
        title="Skæring mellem to linjer",
        opg_id=qid,
        c1x=c1x,
        c1y=c1y,
        c2x=c2x,
        c2y=c2y,
        c1r=c1r,
        c2r=c2r,
        x1=x1,
        x2=x2,
        y1=y1,
        y2=y2,
    )


def get_plot_dimensions(x0, y0, r0, x1, y1, r1):
    big_x = x0 if x0 >= x1 else x1
    big_y = y1 if y1 >= y0 else y0
    small_x = x0 if x0 <= x1 else x1
    small_y = y1 if y1 <= y0 else y0
    big_r = r1 if r1 >= r0 else r0

    min_x = -(abs(small_x) + big_r)
    min_y = -(abs(small_y) + big_r)
    max_x = big_x + big_r
    max_y = big_y + big_r

    return (min_x, min_y, max_x, max_y)


@app.route("/fig/<figure_key>/<x0>/<y0>/<r0>/<x1>/<y1>/<r1>")
def fig(figure_key, x0, y0, r0, x1, y1, r1):
    if figure_key == "Skæring mellem to cirkler":
        x0, y0, r0, x1, y1, r1 = (
            round(float(x0)),
            round(float(y0)),
            round(float(r0)),
            round(float(x1)),
            round(float(y1)),
            round(float(r1)),
        )
        print(x0, y0, r0, x1, y1, r1)
        # now make a circle with no fill, which is good for hi-lighting key results
        plt.title(figure_key)
        circle1 = plt.Circle((x0, y0), r0, color="b", fill=False)
        circle2 = plt.Circle((x1, y1), r1, color="r", fill=False)
        ax = plt.gca()
        ax.cla()  # clear things for fresh plot

        min_x, min_y, max_x, max_y = get_plot_dimensions(x0, y0, r0, x1, y1, r1)
        # change default range so that new circles will work
        ax.set_xlim((min_x, max_x))
        ax.set_ylim((min_y, max_y))

        ax.add_artist(circle1)
        ax.add_artist(circle2)
        img = io.BytesIO()
        plt.savefig(img)
        img.seek(0)
    else:
        plt.title(figure_key)
        plt.plot([1, 2, 3, 4], [1, 3, 2, 4])
        img = io.BytesIO()
        # plt.savefig(img)
        img.seek(0)
    return send_file(img, mimetype="image/png")


def generate_circular_arc():
    length = randint(1, 100)
    qid = register_answer("{}".format(length))
    angle = randint(1, 180)
    r = length / ((angle / 180) * pi)
    return my_render(
        "circulararc.html",
        title="Skæring mellem to linjer",
        opg_id=qid,
        r=r,
        angle=angle,
        length=length,
    )


if __name__ == "__main__":
    app.run(debug=True)
