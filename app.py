from flask import Flask, render_template, request
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator

app = Flask(__name__)
#Chinh sua nhanh 1 merge


@app.route("/", methods=["GET", "POST"])
def index():
    male = None
    female = None

    if request.method == "POST":
        male = int(request.form["male"])
        female = int(request.form["female"])

        labels = ["Nam", "Nữ"]
        values = [male, female]

        # Tạo biểu đồ cột
        plt.figure(figsize=(7, 5))

        bars = plt.bar(labels, values, width=0.5)

        plt.title(
            "Số lượng sinh viên nam và nữ",
            fontsize=16,
            fontweight="bold"
        )

        plt.xlabel("Giới tính", fontsize=12)
        plt.ylabel("Số sinh viên", fontsize=12)

        # Trục Y chỉ hiển thị số nguyên
        plt.gca().yaxis.set_major_locator(
            MaxNLocator(nbins=10, integer=True)
        )

        # Hiển thị số trên đầu cột
        for bar, value in zip(bars, values):
            plt.text(
                bar.get_x() + bar.get_width() / 2,
                bar.get_height(),
                str(value),
                ha="center",
                va="bottom",
                fontsize=12,
                fontweight="bold"
            )

        plt.grid(axis="y", linestyle="--", alpha=0.3)
        plt.tight_layout()

        plt.savefig(
            "static/chart.png",
            dpi=150,
            bbox_inches="tight"
        )

        plt.close()

    return render_template(
        "index.html",
        male=male,
        female=female
    )


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5175
    )