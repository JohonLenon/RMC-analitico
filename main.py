import json
from numpy import sin, cos, tan, pi, radians, abs
import matplotlib.pyplot as plt

def read_json(file, helix):
    with open(file, "r") as f:
        layers = json.load(f)
    types = {
        "isotropic_cylinder": Cylinder,
        "orthotropic_cylinder": helix,
        "solid_isotropic_cylinder": Cylinder,
        "solid_helix": helix,
        "shell_helix": helix
    }
    for layer in layers.values():
        layer["type"] = types[layer["type"]]
    return layers

def pitch(R, angle):
    p = 2*pi*R/tan(radians(abs(angle)))
    return p

def experimental():
    exp = [(0, 0),(0.10960960960960953, 394.73435699850825),(0.23873873873873874, 456.00317298430537),(0.355855855855856, 693.5237123916372),(0.45495495495495497, 843.2205790696362),(0.5720720720720722, 1061.8731939486659),(0.6711711711711712, 1085.7838971046522),(0.7882882882882885, 1210.0968893421725),(0.9024024024024024, 1378.472812435077),(1.0075075075075075, 1402.3079683457047),(0.8993993993993996, 913.1017810263099),(0.659159159159159, 457.0041739853068),(0.45495495495495497, 208.00045328347278),(0.355855855856, -17.1681115077331),(0.18168168168168153, -71.58101497724101),(0.052552552552552534, -189.45360454794354),(-0.0015015015015016342, -333.427767390031),(-0.11861861861861867, -382.26906151434423),(-0.23573573573573592, -519.160670104066),(-0.370870870870871, -643.2470206055104),(-0.484984984984985, -786.4657109940126),(-0.602102102102102, -860.4642378227281),(-0.6861861861861864, -1004.0606644380223),(-0.9174174174174174, -1290.4602715923465),(-1.0225225225225227, -1553.2891381947989),(-0.9174174174174174, -680.3973785105859),(-0.8033033033033032, -587.4931535308892),(-0.7042042042042043, -418.9283623245883),(-0.5870870870870872, -326.0619109675713),(-0.484984984984985, -138.66696885564807),(-0.36786786786786774, -14.35397661812749),(-0.13663663663663672, 127.39154248588193),(-0.007507507507507505, 220.1068993521826),(0.04954954954954971, 345.17536404328894)]
    x_exp, y_exp = zip(*exp)

    ska_07 = [(0, 0.6000000000000005),(0.0070775862068965245, 0.7750000000000004),(0.012379310344827588, 0.8375000000000004),(0.02299137931034481, 1),(0.032229885057471264, 1.1875),(0.0409942528735632, 1.3125),(0.050922413793103444, 1.5),(0.05854597701149425, 1.6625),(0.06660632183908047, 1.725),(0.07492528735632181, 1.9125),(0.08278735632183909, 2.1125),(0.0904109195402299, 2.275),(0.09735344827586209, 2.475),(0.1036005747126437, 2.65),(0.10754597701149424, 2.8124999999999996),(0.11171264367816094, 2.9375),(0.1102672413793104, 2.65),(0.10907183908045978, 2.4499999999999997),(0.10765517241379316, 2.2875),(0.10577586206896553, 2.1125),(0.10366379310344823, 1.9250000000000003),(0.10154885057471266, 1.725),(0.09875574712643678, 1.5750000000000002),(0.09572413793103451, 1.3875000000000002),(0.09316091954022987, 1.2374999999999998),(0.08898850574712644, 1.0874999999999995),(0.08480747126436783, 0.8999999999999995),(0.08087356321839084, 0.7875000000000005),(0.07694540229885058, 0.7000000000000002),(0.07393103448275865, 0.5874999999999995),(0.06906609195402297, 0.4250000000000007),(0.0621264367816092, 0.2375000000000007),(0.05150862068965517, 0.05000000000000071),(0.039959770114942506, -0.1875),(0.028181034482758605, -0.4249999999999998),(0.011094827586206862, -0.75),(-0.003908045977011498, -1.0124999999999993),(-0.015913793103448315, -1.2374999999999998),(-0.027229885057471287, -1.4624999999999995),(-0.039913793103448295, -1.6375000000000002),(-0.05261781609195407, -1.8999999999999995),(-0.06508045977011498, -2.1125),(-0.08147413793103452, -2.425),(-0.08839655172413798, -2.5374999999999988),(-0.09370402298850579, -2.624999999999999),(-0.09924425287356325, -2.7249999999999988),(-0.10408620689655176, -2.7874999999999988),(-0.1089252873563219, -2.8374999999999995),(-0.10796551724137936, -2.6625000000000005),(-0.10607471264367821, -2.437499999999999),(-0.10465517241379316, -2.2624999999999993),(-0.1018563218390805, -2.0874999999999995),(-0.10043965517241385, -1.9249999999999998),(-0.09533333333333338, -1.7124999999999995),(-0.08954022988505753, -1.5124999999999993),(-0.08443678160919545, -1.3125),(-0.07702586206896556, -1.0750000000000002),(-0.06938505747126442, -0.8374999999999995),(-0.05897413793103452, -0.5499999999999998),(-0.04995689655172417, -0.3250000000000002),(-0.038859195402298874, -0.04999999999999982),(-0.029393678160919562, 0.125),(-0.01969540229885061, 0.3125),(-0.011155172413793102, 0.46250000000000036),(0, 0.6000000000000005)]
    x_ska07, y_ska07 = zip(*ska_07)
    y_ska07 = [a*1000 for a in y_ska07]
    return x_exp, y_exp, x_ska07, y_ska07

class Model:
    def __init__(self, layers, curvatures):
        self.layers = layers
        self.curvatures = curvatures
    def compute_stiffness(self):
        EI = []
        for layer in self.layers.values():
            cls = layer["type"]
            params = {k: v for k, v in layer.items() if k != "type"}
            EI.append((layer['name'], *cls(**params).compute()))
        pre, post = 0, 0
        for _, _, EI_pre, EI_post in EI:
            pre += EI_pre
            post += EI_post
        kcr_min = min(kcr for _, kcr, EI_pre, EI_post in EI if kcr is not None)
        return (kcr_min, pre, post, EI)
    def write_table(self, ax, params):
        ax.axis('off')
        formatted = [(name, f"{kappa:.4f}" if kappa is not None else "-", f"{ei0/1000:.4f}", f"{ei1/1000:.4f}")
                    for name, kappa, ei0, ei1 in params
                    ]
        total_ei0 = sum(ei0 for _, _, ei0, _ in params)
        total_ei1 = sum(ei1 for _, _, _, ei1 in params)
        formatted.append(("Total", "-", f"{total_ei0/1000:.4f}", f"{total_ei1/1000:.4f}"))

        n_rows = len(formatted)

        tabela = ax.table(
            cellText=formatted,
            colLabels=['Layer', r'$\kappa_{cr}$ (1/m)', r'$EI_0$ (kNm$^2$)', r'$EI_1$ (kNm$^2$)'],
            loc='center',
            cellLoc='center',
        )
        tabela.auto_set_font_size(False)
        tabela.set_fontsize(12)
        tabela.scale(1, 1.5)

        for (row, col), cell in tabela.get_celld().items():
            cell.set_edgecolor('black')
            cell.visible_edges = ''

            if row == 0:
                cell.visible_edges = 'TB'
                cell.set_text_props(fontweight='bold')
            elif row == n_rows:
                cell.visible_edges = 'B'
                cell.set_text_props(fontweight='bold')
            if col == 0:
                cell.set_text_props(ha='left')
    def print_stiffness(self, params):
        kcr = min(kcr for _, kcr, _, _ in params if kcr is not None)
        total_ei0 = sum(ei0 for _, _, ei0, _ in params)
        total_ei1 = sum(ei1 for _, _, _, ei1 in params)
        print("Total", "-", r"kcr$_{min}$:" f"{kcr:.4f}", r"EI$_0$:" f"{total_ei0/1000:.4f}", r"EI$_1$:", f"{total_ei1/1000:.4f}")    
    def draw_hysteresis(self, ax, kcr, EI_pre, EI_post, label):
        kmin, kmax = self.curvatures

        M_cr  = EI_pre  * kcr
        M_max = M_cr + EI_post * (kmax - kcr)
        M_res = M_max - EI_pre * 2*kcr
        M_min = M_res + EI_post * (kmin - (kmax - 2*kcr))
        M_rec = M_min + EI_pre * 2*kcr

        curvaturas = [0, kcr, kmax,  kmax - 2*kcr, kmin, kmin + 2*kcr, 0]
        momentos   = [0, M_cr, M_max, M_res,  M_min, M_rec,  M_cr]

        ax.plot(curvaturas, momentos, 'o-', label = label)

        # ax.set_aspect(aspect=3/6000)
        ax.set_xlim(-0.2,0.2)
        ax.set_ylim(-4000,4000)
        ax.tick_params(axis='both', labelsize=16)
        ax.set_xlabel("Curvatura (1/m)", fontsize=16)
        ax.set_ylabel("Momento (Nm)", fontsize=16)
        # ax.set_xticks([-0.2, -0.1, 0, 0.1, 0.2])
        # ax.set_yticks([-4000, -2000, 0, 2000, 4000])
        # ax.set_title("Relação momento-curvatura", fontsize=12)
        ax.grid(True)
        ax.legend(fontsize=12)
        plt.tight_layout()
    def build(self, ax_plot, label, ax_table=None):
        kcr, EI_pre, EI_post, EI = self.compute_stiffness()
        self.draw_hysteresis(ax_plot, kcr, EI_pre, EI_post, label)
        # self.write_table(ax_table, EI)
        self.print_stiffness(EI)

class Helix:
    def __init__(self, *, name, mid_diameter, thickness, young_modulus, poisson, lay_angle, n, base = None, A = None, Iy = None, Ix = None, J = None, **kwargs):
        self.name = name
        self.mid_diameter = mid_diameter
        self.radius = mid_diameter/2
        self.n = n
        self.young_modulus = young_modulus
        self.poisson = poisson
        self.lay_angle = radians(abs(lay_angle))
        self.G = self.young_modulus/(2 * (1+self.poisson))
        self.tension = True if J is None else False
        self.base = base if base is not None else 0
        self.A = A if A is not None else self.base * thickness
        self.Ix = Ix if Ix is not None else self.base * thickness**3 / 12
        self.Iy = Iy if Iy is not None else thickness * self.base**3 / 12
        self.J = J if J is not None else self.base * thickness**3 * (1/3 - 0.21 * thickness / self.base * (1 - thickness**4 / (12 * self.base**4)))
        self.thickness = thickness
        self.pitch = pitch(self.radius, self.lay_angle)
    def critical_curv(self):
        E, t, alpha = self.young_modulus, self.thickness, self.lay_angle
        f = 0.1
        q = 4e6
        kcr = f*q / (E * t * sin(alpha) * cos(alpha)**2) if self.tension else None
        return kcr
    def pre_slip(self):
        return 0.0
    def post_slip(self):
        return 0.0
    def compute(self):
        kcr = self.critical_curv()
        EI_pre = self.pre_slip()
        EI_post = self.post_slip()
        return (kcr, EI_pre, EI_post)
    
class Witz_helix(Helix):
    def pre_slip(self):
        n, E, A, R, alpha, Iy, Ix, G, J = self.n, self.young_modulus, self.A, self.radius, self.lay_angle, self.Iy, self.Ix, self.G, self.J

        EI = 1/2 *(n * E * A* R**2 * cos(alpha)**4 + E * Iy + E * Ix * cos(alpha)**2 + G * J * sin(alpha)**2)
        return EI 
    def post_slip(self):
        E, alpha, Iy, Ix, G, J = self.young_modulus, self.lay_angle, self.Iy, self.Ix, self.G, self.J

        EI = 1/2 *(E * Iy + E * Ix * cos(alpha)**2 + G * J * sin(alpha)**2)
        return EI

class Dong_helix(Helix):
    def pre_slip(self):
        n, E, alpha, A, R, Iy, Ix, G, J = self.n, self.young_modulus, self.lay_angle, self.A, self.radius, self.Iy, self.Ix, self.G, self.J

        EI = 1/2 *n * (E * A* R**2 * cos(alpha)**3 + E * Iy * (1 + sin(alpha)**2)**2 * cos(alpha) + E * Ix * cos(alpha)**7 + G * J * sin(alpha)**2 * cos(alpha)**5)
        return EI
    def post_slip(self):
        n, E, alpha, Iy, Ix, G, J = self.n, self.young_modulus, self.lay_angle, self.Iy, self.Ix, self.G, self.J
        EI = 1/2 * n * (E * Iy * (1 + sin(alpha)**2)**2 * cos(alpha) + E * Ix * cos(alpha)**7 + G * J * sin(alpha)**2 * cos(alpha)**5)
        return EI

class Zhang_helix(Helix):
    def pre_slip(self):
        n, E, A, R, alpha = self.n, self.young_modulus, self.A, self.radius, self.lay_angle

        EI = 1/2 *n * E * A* R**2 * cos(alpha)**3
        return EI

class Witz_fixed_helix(Helix):
    def pre_slip(self):
        n, E, A, R, alpha, Iy, Ix, G, J = self.n, self.young_modulus, self.A, self.radius, self.lay_angle, self.Iy, self.Ix, self.G, self.J

        EI = n / 2 * (E * A * R**2 * cos(alpha)**3 + G * J * sin(alpha)**2 / cos(alpha) + E * Iy * cos(alpha) + E * Ix / cos(alpha))
        return EI
    def post_slip(self):
        n, E, alpha, Iy, Ix, G, J = self.n, self.young_modulus, self.lay_angle, self.Iy, self.Ix, self.G, self.J

        EI = n / 2 * (G * J * sin(alpha)**2 / cos(alpha) + E * Iy * cos(alpha) + E * Ix / cos(alpha))
        return EI

class Lei_helix(Helix):
    def pre_slip(self):
        n, E, A, R, alpha, Iy, Ix, G, J = self.n, self.young_modulus, self.A, self.radius, self.lay_angle, self.Iy, self.Ix, self.G, self.J

        EI = n / 2 * (E* A * R**2 * cos(alpha)**3 + (E * Iy * (1 + sin(alpha)**2)**2 * cos(alpha) + E * Ix * cos(alpha)**7 + G * J * sin(alpha)**2 * cos(alpha)**5))
        return EI
    def post_slip(self):
        n, E, alpha, Iy, Ix, G, J = self.n, self.young_modulus, self.lay_angle, self.Iy, self.Ix, self.G, self.J

        EI = n / 2 * (E * Iy * (1 + sin(alpha)**2)**2 * cos(alpha) + E * Ix * cos(alpha)**7 + G * J * sin(alpha)**2 * cos(alpha)**5)
        return EI

class Cylinder:
    def __init__(self, *, name, mid_diameter, thickness, young_modulus, poisson, **kwargs):
        self.name = name
        self.mid_diameter = mid_diameter
        self.radius = mid_diameter/2
        self.thickness = thickness
        self.young_modulus = young_modulus
        self.poisson = poisson
    def stiffness(self):
        E, R, t = self.young_modulus, self.radius, self.thickness
        EI = E * pi * R * t * (R**2 + t**2 / 4)
        return EI
    def compute(self):
        EI = self.stiffness()
        return (None, EI, EI)
    
fig, ax = plt.subplots(figsize=(7, 5))

x_exp, y_exp, x_ska07, y_ska07 = experimental()
ax.plot(x_ska07, y_ska07, 's-', color="#4D4D4D", label=r"Experimental", markerfacecolor='#ffffff')

layers = read_json(r"..\Algoritmos\risers\skallerud-si-analitico.json", Witz_helix)
w = Model(layers, (-1/9, 1/9))
w.build(ax, label="Witz e Tan (1992)")

layers = read_json(r"..\Algoritmos\risers\skallerud-si-analitico.json", Dong_helix)
d = Model(layers, (-1/9, 1/9))
d.build(ax, label=r"Dong $\it{et\ al.}$ (2013)")

layers = read_json(r"..\Algoritmos\risers\skallerud-si-analitico.json", Zhang_helix)
d = Model(layers, (-1/9, 1/9))
d.build(ax, label=r"Zhang $\it{et\ al.}$ (2023)")

ax.legend()
plt.tight_layout()
# plt.savefig("Witz-analitico.png", bbox_inches='tight')
# plt.savefig("Skallerud-analitico.png", bbox_inches='tight')
plt.show()