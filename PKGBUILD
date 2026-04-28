# Maintainer: Darian Alberto Camacho Salas <xonidu@gmail.com>
# Contributor: XONIDU <xonidu@gmail.com>

pkgname=xonispam
pkgver=1.0.0
pkgrel=1
pkgdesc="Herramienta educativa de automatización de teclado para pruebas de spam"
arch=('any')
url="https://github.com/XONIDU/xonispam"
license=('MIT')
depends=('python' 'python-pyautogui')
makedepends=('git')
source=("$pkgname-$pkgver.tar.gz::https://github.com/XONIDU/xonispam/archive/v$pkgver.tar.gz")
sha256sums=('SKIP')

package() {
    # Crear directorios
    install -dm755 "$pkgdir/usr/share/$pkgname"
    install -dm755 "$pkgdir/usr/bin"
    install -dm755 "$pkgdir/usr/share/doc/$pkgname"
    install -dm755 "$pkgdir/usr/share/licenses/$pkgname"
    
    # Instalar programa principal
    install -Dm644 "$srcdir/$pkgname-$pkgver/xonispam.py" "$pkgdir/usr/share/$pkgname/xonispam.py"
    
    # Instalar lanzador
    install -Dm755 "$srcdir/$pkgname-$pkgver/start.py" "$pkgdir/usr/bin/xonispam"
    
    # Instalar documentación
    install -Dm644 "$srcdir/$pkgname-$pkgver/README.md" "$pkgdir/usr/share/doc/$pkgname/README.md"
    
    # Instalar licencia
    install -Dm644 "$srcdir/$pkgname-$pkgver/LICENSE" "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
