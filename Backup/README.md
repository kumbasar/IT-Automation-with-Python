# Generate report from log file

This script backups `data/prod/` to `data/prod_backup/` using multiprocessing pool.
## Usage

```bash
./dailysync.py
```
## Example output

```bash
kumbasar@kumbasar:~$ ./scripts/dailysync.py
Backup src: ./data/prod/kappa/docs to dest: data/prod_backup/kappa/docs
Backup src: ./data/prod/kappa/videos to dest: data/prod_backup/kappa/videos
Backup src: ./data/prod/kappa/pictures to dest: data/prod_backup/kappa/pictures
Backup src: ./data/prod/delta/pictures to dest: data/prod_backup/delta/pictures
Backup src: ./data/prod/gamma/docs to dest: data/prod_backup/gamma/docs
Backup src: ./data/prod/alpha/videos to dest: data/prod_backup/alpha/videos
Backup src: ./data/prod/kappa to dest: data/prod_backup/kappa
Backup src: ./data/prod/delta to dest: data/prod_backup/delta
Backup src: ./data/prod/omega to dest: data/prod_backup/omega
Backup src: ./data/prod/gamma to dest: data/prod_backup/gamma
Backup src: ./data/prod/alpha to dest: data/prod_backup/alpha
Backup src: ./data/prod/beta to dest: data/prod_backup/beta
Backup src: ./data/prod/sigma to dest: data/prod_backup/sigma
```