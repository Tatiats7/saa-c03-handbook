# AWS Architecture Icons: notice

The diagrams in this book use the official AWS Architecture Icons, unmodified.

- Source page: <https://aws.amazon.com/architecture/icons/>
- Package: <https://d1.awsstatic.com/onedam/marketing-channels/website/public/shared/architecture-icon-release/Icon-package_07312026.5846e92413caa21490223536cc97f1269e44fa92.zip>
- Package release: 2026-07-31
- Downloaded: 2026-10-05
- SHA-256 of the zip: `d2d166c453526471749d520e0db022c459abef759d2946cf2dd1d1c992dc6526`
- Icons extracted into `icons.json`: 274

## AWS usage statement

Quoted from the source page on the download date:

> We allow customers and partners to use these toolkits and assets to create architecture diagrams.

## What the build does to the files

Each icon is the 48 px SVG from the package. The build removes the XML prolog, comments, `<title>` and `<desc>`, and unreferenced `id` attributes so that many icons can share one page. Shapes, colours and proportions are not changed. Icons are drawn at one size.

## Names not found in this release

`elastic-transcoder`, `vmware-cloud-on-aws`
