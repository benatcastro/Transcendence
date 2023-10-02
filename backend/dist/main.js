"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
const core_1 = require("@nestjs/core");
const app_module_1 = require("./app.module");
const prisma_filter_1 = require("./prisma/prisma.filter");
const app_filter_1 = require("./app.filter");
async function bootstrap() {
    const app = await core_1.NestFactory.create(app_module_1.AppModule);
    const { httpAdapter } = app.get(core_1.HttpAdapterHost);
    app.useGlobalFilters(new app_filter_1.AllExceptionsFilter(httpAdapter));
    app.useGlobalFilters(new prisma_filter_1.PrismaClientValidationFilter(httpAdapter));
    app.useGlobalFilters(new prisma_filter_1.PrismaClientExceptionFilter(httpAdapter));
    await app.listen(3000);
}
bootstrap();
//# sourceMappingURL=main.js.map