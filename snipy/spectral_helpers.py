import numpy as np

def s2r_from_ek(k,ek,L=np.pi):
    """
    Given energy spectrum $E(k)$, compute second order structure function,
    using the relation $S_2(r) = \int_0^{\infty} \left(1-\cos{kr}\right) E(k) \Delta k$
    """
    dk  = k[1]-k[0]
    r   = np.linspace(0,L,512)
    s2r = np.asarray([4*np.sum((1-np.cos(k*ri)*ek*dk)) for ri in r])
    return r, s2r

def cr_from_ek(k,ek,L=np.pi):
    import warnings
    with warnings.catch_warnings():
        warnings.filterwarnings("ignore",category=RuntimeWarning)
        dk = k[1]-k[0]
        r,cr = np.linspace(0,L,512), np.zeros(512)
        for i,ri in enumerate(r):
            sinf = np.sin(k*ri)/(k*ri)
            sinf[0] = 1
            cr[i] = np.sum(ek*sinf)*dk
        cr[0] = np.sum(ek)*dk
        return r, cr/cr[0]

def ek_from_cr(r,cr,dk=1.e0):
    dr = r[1]-r[0]
    k  = dk*np.arange(len(r)+1)
    ek = np.asarray([(2/np.pi)*np.sum(ki*r*np.sin(ki*r)*cr)*dr for ki in k])
    return k, ek
