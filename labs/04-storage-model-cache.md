# Lab 04 — Storage، Volume و Model Cache

## هدف

مدل هر بار از اینترنت دانلود نشود و storage strategy روشن باشد.

## سناریو

یک مدل ۱ تا ۲۰ گیگابایتی دارید. باید تصمیم بگیرید وزن مدل داخل image باشد، روی Network Volume باشد یا در S3-compatible storage نگهداری شود.

## کارها

1. یک Network Volume بسازید.
2. مدل یا artifact نمونه را روی volume ذخیره کنید.
3. Pod را حذف یا عوض کنید.
4. Pod جدید را با همان volume بالا بیاورید.
5. ثابت کنید مدل بدون دانلود مجدد قابل استفاده است.
6. اگر سناریوی چند دیتاسنتر دارید، گزینه S3 را بررسی کنید.

## تصمیم‌نامه تحویل

| سناریو | Storage مناسب | دلیل |
| --- | --- | --- |
| تست سریع | Container Disk | موقت و ساده |
| مدل بزرگ | Network Volume | پایدار و قابل reuse |
| چند دیتاسنتر | S3 یا چند Volume | کاهش وابستگی locality |
| artifact بلندمدت | S3-compatible | backup و exchange |
| training checkpoint | Network Volume + backup | سرعت و پایداری |

## هشدار

Network Volume می‌تواند availability را به دیتاسنتر همان volume گره بزند. این موضوع را در runbook و طراحی failover مستند کنید.
