import assert from "assert";
import { dummyForm } from "./models";
import { schemaToYup } from "./validation";

describe(schemaToYup, () => {
  it("works for the empty form", async () => {
    const emptyForm = JSON.parse(JSON.stringify(dummyForm));
    emptyForm.fields = [];

    const validator = schemaToYup(emptyForm);
    assert(await validator.isValid({}));
    assert(!(await validator.isValid({ foo: 5 })));
  });

  it("works for the dummy form", async () => {
    const validator = schemaToYup(dummyForm);

    const validExamples = [
      {
        requiredField: "foo",
        requiredCheckbox: true,
      },
      {
        requiredField: "foo",
        optionalField: "bar",
        requiredCheckbox: true,
      },
    ];
    for (const validExample of validExamples) {
      assert(await validator.isValid(validExample), `${validExample}`);
    }

    const invalidExamples = [
      undefined,
      null,
      5,
      "foo",
      {
        // requiredField: "foo",
        optionalField: "bar",
        requiredCheckbox: true,
      },
      {
        requiredField: "foo",
        optionalField: "bar",
        // requiredCheckbox: true,
      },
      {
        requiredField: "foo",
        optionalField: "bar",
        requiredCheckbox: true,
        unknownField: "quux",
      },
    ];
    for (const invalidExample of invalidExamples) {
      assert(!(await validator.isValid(invalidExample)), `${invalidExample}`);
    }
  });
});
