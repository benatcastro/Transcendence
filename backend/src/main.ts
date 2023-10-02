import { HttpAdapterHost, NestFactory } from '@nestjs/core';
import { AppModule } from './app.module';
import { PrismaClientExceptionFilter, PrismaClientValidationFilter } from './prisma/prisma.filter';
import { AllExceptionsFilter } from './app.filter';


async function bootstrap() {
    const app = await NestFactory.create(AppModule);

    const { httpAdapter } = app.get(HttpAdapterHost);
    app.useGlobalFilters(new PrismaClientValidationFilter(httpAdapter));
    app.useGlobalFilters(new PrismaClientExceptionFilter(httpAdapter));
    await app.listen(3000);
  
}
bootstrap();
