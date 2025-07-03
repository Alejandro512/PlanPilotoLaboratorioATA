class ReportMetrics:
    def __init__(self):
        self.reports_created = 0
        self.reports_downloaded = 0
        self.total_size_mb = 0.0  # Si quieres estimar peso
        self.containers_used = set()  # Si quieres ver blobs/containers únicos

    def log_created(self, size_mb, container_id):
        self.reports_created += 1
        self.total_size_mb += size_mb
        self.containers_used.add(container_id)

    def log_downloaded(self):
        self.reports_downloaded += 1

    def show(self):
        print(f"Reportes generados: {self.reports_created}")
        print(f"Reportes descargados: {self.reports_downloaded}")
        print(f"Tamaño total estimado (MB): {self.total_size_mb:.2f}")
        print(f"Containers únicos usados: {len(self.containers_used)}")
