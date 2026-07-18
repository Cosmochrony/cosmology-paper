# Spectral zeta of the minimal scalar Laplacian on the unit S^4 (Dowker-type values).
# Working check for the H_infty driven-equilibrium construction recon (untracked, working-notes rule).
#
# Spectrum: lambda_n = n(n+3), degeneracy d_n = (n+1)(n+2)(2n+3)/6, n >= 1 (zero mode excluded).
# Substitution m = n + 3/2 (m = 5/2, 7/2, ...): lambda = m^2 - 9/4, d = (m^3 - m/4)/3.
# zeta(s) = (1/3) sum_k binom(s+k-1,k) (9/4)^k [zeta_H(2s+2k-3, 5/2) - (1/4) zeta_H(2s+2k-1, 5/2)]
# (binomial expansion of (1 - (9/4)m^-2)^{-s}, convergent since 9/4 < (5/2)^2).
#
# Checks:
#   (1) zeta(0) = B4 - N0 = 29/90 - 1 = -61/90 (heat-kernel prediction, a4 integrated on S^4).
#   (2) zeta'(0) numeric (additive constant of log det'; plays no role in H-stationarity).
#   (3) Scaling law: on S^4 of radius a = 1/H, S_Pi(H) = zeta(0) log H - (1/2) zeta'(0)
#       [+ scheme-dependent local terms ~ H^-4, H^-2 from the renormalisation of Beau2026h].

import mpmath as mp

mp.mp.dps = 40

A = mp.mpf(9) / 4


def zeta_spec(s):
    s = mp.mpf(s) if not isinstance(s, mp.mpc) else s
    total = mp.mpf(0)
    k = 0
    while True:
        c = mp.binomial(s + k - 1, k) * A**k
        t = mp.zeta(2 * s + 2 * k - 3, mp.mpf(5) / 2) - mp.zeta(2 * s + 2 * k - 1, mp.mpf(5) / 2) / 4
        term = c * t / 3
        total += term
        if k > 6 and abs(term) < mp.mpf(10) ** (-(mp.mp.dps - 5)):
            break
        k += 1
        if k > 300:
            raise RuntimeError("no convergence")
    return total


def direct_partial(s, N=2000):
    # direct partial sum, only valid for Re(s) > 2 (sanity check of the representation)
    return mp.nsum(lambda n: (n + 1) * (n + 2) * (2 * n + 3) / 6 / (n * (n + 3)) ** s, [1, N])


# Sanity: representation vs direct sum at s = 3
s_test = mp.mpf(3)
rep = zeta_spec(s_test)
direct = direct_partial(s_test, 4000)
print("sanity s=3: representation =", mp.nstr(rep, 20), " direct =", mp.nstr(direct, 20),
      " diff =", mp.nstr(abs(rep - direct), 5))

# zeta(0): evaluate near 0 (each k-term analytic at 0; pole of zeta_H at arg 1 cancelled by binomial zero)
eps = mp.mpf(10) ** -12
z0 = (zeta_spec(eps) + zeta_spec(-eps)) / 2
print("zeta(0) numeric   =", mp.nstr(z0, 25))
print("zeta(0) predicted =", mp.nstr(mp.mpf(-61) / 90, 25), " (29/90 - 1)")
print("difference        =", mp.nstr(abs(z0 - mp.mpf(-61) / 90), 5))

# zeta'(0): central difference (function analytic at 0)
h = mp.mpf(10) ** -10
zp0 = (zeta_spec(h) - zeta_spec(-h)) / (2 * h)
print("zeta'(0) numeric  =", mp.nstr(zp0, 20))

# log det' A_1 = -zeta'(0);  S_Pi[S^4_1] = (1/2) log det' = -(1/2) zeta'(0)
print("S_Pi[S^4, a=1] = -(1/2) zeta'(0) =", mp.nstr(-zp0 / 2, 20))

# Scaling: A_a = a^-2 A_1 => zeta_a(s) = a^{2s} zeta_1(s) => -zeta_a'(0) = -2 log(a) zeta(0) - zeta'(0)
# With a = 1/H: S_Pi(H) = zeta(0) log H - (1/2) zeta'(0). Log-slope printed exactly:
print("log-slope dS_Pi/dlogH = zeta(0) = -61/90 =", mp.nstr(mp.mpf(-61) / 90, 10))

# Driven term, intensive readings (arithmetic identity, printed for the record):
# (i) per Euclidean period: Delta S_hist = h_b * H * (2 pi / H) = 2 pi h_b
# (ii) per horizon patch over the instanton: (h_b H / V_H) * Vol(S^4_{1/H})
#      = h_b H * (3 H^3 / 4 pi) * (8 pi^2 / 3) H^{-4} = 2 pi h_b  (same constant)
hb = mp.log(1 + mp.sqrt(2))
print("2 pi h_b =", mp.nstr(2 * mp.pi * hb, 15), " (H-independent under BOTH intensive readings)")
