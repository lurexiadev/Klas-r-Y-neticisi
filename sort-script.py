import os
import shutil

def dosyalari_duzenle():
    kaynak = input("Düzenlenecek klasörün yolunu gir: ").strip().strip('"')

    if not os.path.isdir(kaynak):
        print("Hata: Klasör bulunamadı.")
        return

    kurallar = {
        "Resimler": [".png", ".jpg", ".jpeg", ".gif", ".webp", ".bmp"],
        "Videolar": [".mp4", ".mkv", ".avi", ".mov", ".webm"],
        "Belgeler": [".pdf", ".doc", ".docx", ".txt", ".odt", ".rtf", ".pptx"],
        "Tablolar": [".xlsx", ".xls", ".csv"],
        "Sesler": [".mp3", ".wav", ".flac", ".aac", ".ogg"],
        "Arsivler": [".zip", ".rar", ".7z", ".tar", ".gz"],
        "Kodlar": [
    # Python
            ".py", ".pyw", ".pyi", ".pyx", ".pxd", ".pxi", ".ipynb",

            # JavaScript ve TypeScript
            ".js", ".mjs", ".cjs", ".jsx", ".ts", ".mts", ".cts", ".tsx",

            # Web
            ".html", ".htm", ".xhtml", ".css", ".scss", ".sass",
            ".less", ".vue", ".svelte", ".astro",

            # C ve C++
            ".c", ".h", ".cc", ".cpp", ".cxx", ".hh", ".hpp",
            ".hxx", ".ipp", ".inl",

            # C# ve .NET
            ".cs", ".csx", ".vb", ".fs", ".fsx", ".fsi",

            # Java ve JVM
            ".java", ".class", ".jar", ".kt", ".kts", ".scala",
            ".sc", ".groovy", ".gradle", ".clj", ".cljs", ".cljc",

            # Sistem ve düşük seviye
            ".rs", ".go", ".zig", ".nim", ".d", ".asm", ".s",
            ".ll", ".wat", ".wasm",

            # Apple ve mobil
            ".swift", ".m", ".mm", ".h", ".dart",

            # PHP ve sunucu tarafı
            ".php", ".phtml", ".phar", ".rb", ".erb", ".rake",
            ".pl", ".pm", ".t", ".lua", ".luau",

            # Diğer programlama dilleri
            ".r", ".R", ".rmd", ".jl", ".ex", ".exs", ".erl",
            ".hrl", ".hs", ".lhs", ".elm", ".purs", ".ml",
            ".mli", ".re", ".rei", ".fs", ".fsx", ".cl",
            ".lisp", ".lsp", ".scm", ".ss", ".rkt", ".pro",
            ".prolog", ".plg", ".f", ".for", ".f90", ".f95",
            ".f03", ".f08", ".cob", ".cbl", ".ada", ".adb",
            ".ads", ".pas", ".pp", ".dpr", ".lpr",

            # Veritabanı ve sorgu dilleri
            ".sql", ".psql", ".prisma", ".graphql", ".gql",
            ".cypher", ".cql",

            # Shell ve komut dosyaları
            ".sh", ".bash", ".zsh", ".fish", ".ps1", ".psm1",
            ".psd1", ".bat", ".cmd", ".awk", ".sed",

            # Yapılandırma ve veri biçimleri
            ".json", ".jsonc", ".json5", ".xml", ".yaml", ".yml",
            ".toml", ".ini", ".cfg", ".conf", ".properties",
            ".env", ".dotenv", ".editorconfig",

            # Derleme, otomasyon ve altyapı
            ".dockerfile", ".tf", ".tfvars", ".hcl", ".nix",
            ".mk", ".make", ".cmake", ".gradle", ".bazel",
            ".bzl", ".just", ".ipynb",

            # Şablonlar ve diğer kaynak dosyaları
            ".jinja", ".j2", ".mustache", ".hbs", ".handlebars",
            ".ejs", ".pug", ".jade", ".liquid", ".twig",
            ".md", ".mdx", ".tex", ".sty", ".cls"
        ]
    }

    tasinan = 0

    for dosya in os.listdir(kaynak):
        dosya_yolu = os.path.join(kaynak, dosya)

        if not os.path.isfile(dosya_yolu):
            continue

        uzanti = os.path.splitext(dosya)[1].lower()
        hedef_klasor = "Diger"

        for klasor, uzantilar in kurallar.items():
            if uzanti in uzantilar:
                hedef_klasor = klasor
                break

        hedef_yol = os.path.join(kaynak, hedef_klasor)
        os.makedirs(hedef_yol, exist_ok=True)

        hedef_dosya = os.path.join(hedef_yol, dosya)

        # Aynı isimli dosyanın üzerine yazma.
        ad, ext = os.path.splitext(dosya)
        sayac = 2

        while os.path.exists(hedef_dosya):
            hedef_dosya = os.path.join(
                hedef_yol, f"{ad} ({sayac}){ext}"
            )
            sayac += 1

        try:
            shutil.move(dosya_yolu, hedef_dosya)
            print(f"[TAŞINDI] {dosya} -> {hedef_klasor}/")
            tasinan += 1
        except OSError as hata:
            print(f"[HATA] {dosya}: {hata}")

    print(f"\nTamamlandı. Taşınan dosya sayısı: {tasinan}")


if __name__ == "__main__":
    dosyalari_duzenle()